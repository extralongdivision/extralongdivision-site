"""Take a canonical post and make it easier to syndicate."""
import argparse
import os
import re
import shutil

from markdownify import markdownify as md


class URLBuilder:
    def __init__(self, source: str):
        self._domain = "extralongdivision.com"
        self._url = self._domain + "/"
        self._source = source
        self._socials = (  # it's social if i'm posting to my own account
            "twitter",
            "bluesky",
            "mastodon",
            "threads"
            "instagram",
            "facebook",
            "youtube",
            "peertube",
            "tiktok",
            "reddit",
            "lemmy",
            "hackaday",
            "hackster",
            "adafruit_playground",
            "dev",
            "medium",
            "substack",
            "instructables",
            "hacker_news",
            "makerio"
            "makerpro",
            "codeberg",
            "gitlab",
            "github",
            "grabcad",
            "thingiverse",
        )

    def inject_syndication_utms(self, line: str, utm_content: str) -> str:
        # if line has my domain, and has not utm's, add this classes
        if self._url not in line:
            return line
        # line contains my domain name

        # check if url has utms
        url = re.search(r"(?<=\().*?(?=\))", line).group()
        if self._domain not in url:
            return line  # this isn't a link to my domain

        if "?" in url and "utm" in url:
            return line  # already has utm parameters

        # check if a file not a url
        filename = url.split("/")[-1]
        if len(filename.split(".")) > 1:  # url is for a file
            if ".html" not in filename or ".xml" not in filename:
                return line  # a media file, ignore
        # an ugly url or rss file, still needs utm

        new_url = self.syndication_url(url=url, utm_content=utm_content)
        return line.replace(url, new_url)

    def _query(self, source: str, medium: str, campaign: str = "", uid: str = "", content: str = "", is_paid: bool = False) -> str:
        if "social" in medium.lower():  # posting to social medium
            if source not in self._socials:
                raise ValueError(f"{source} is not a valid social medium.")

            if is_paid:
                medium = "paid_social"
            else:
                medium = "organic_social"
        q = f"?utm_source={source}&utm_medium={medium}"
        if campaign:
            q += f"&utm_campaign={campaign}"
        if uid:
            q += f"&utm_id={uid}"
        if content:
            q += f"&utm_content={content}"
        return q

    def syndication_url(self, utm_content: str, url: str = "") -> str:
        if self._source in self._socials:
            return self.social_syndication_url(url=url, utm_content=utm_content)
        else:
            raise NotImplementedError(f"No syndication url implemented for {self._source}")

    def social_syndication_url(self, utm_content: str, url: str = "") -> str:
        url = url if url else self._url
        return url + self._query(source=self._source, medium="organic_social", campaign="syndication", uid="1", content=utm_content, is_paid=False)

    def backlink_url(self) -> str:
        raise NotImplementedError


class Crosspost:
    """A post that's easier to syndicate."""

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog="Crosspost Preprocessor",
            description="Take a canonical html post and transform it to something easier to syndicate.",
        )
        parser.add_argument("-i", "--input-filepath")
        parser.add_argument("-t", "--target-site")
        args = parser.parse_args()

        self._url_builder = URLBuilder(source=args.target_site)

        self._build_dir = "temp" + os.sep
        self._init_build_dir()

        self._local_domain = "localhost"
        self._canonical_domain = "extralongdivision.com/"

        self._input_filepath = args.input_filepath
        self._slug = self._get_slug()
        self._output_filepath = self._md_filepath(self._input_filepath)

        self._to_md()

        self._port = self._find_port()

    def iter_md(self) -> None:
        """replace all instances of localhost with canonical website."""
        tmp = self._output_filepath + ".tmp"
        shutil.copyfile(self._output_filepath, tmp)
        with open(self._output_filepath, "w") as fout:
            with open(tmp) as fin:
                for line in fin.readlines():
                    line = self._replace_domain(line)
                    line = self._force_https(line)
                    line = self._url_builder.inject_syndication_utms(line, self._slug)
                    # TODO create PNGs of webp
                    # TODO create replace webp with PNG
                    fout.write(line)

    @staticmethod
    def _force_https(line: str) -> str:
        return line.replace("](http:", "](https:")

    def _replace_domain(self, line: str) -> str:
        key = f"{self._local_domain}:{self._port}/"
        return line.replace(key, self._canonical_domain)

    def _init_build_dir(self) -> None:
        try:
            os.makedirs(self._build_dir)
        except FileExistsError:
            pass

    def _get_slug(self) -> str:
        with open(self._input_filepath) as fin:
            for line in fin.readlines():
                if "rel=\"canonical\"" not in line:
                    continue

                canonical_url = re.search("(?<=href=\").*?(?=\")", line).group()
                slug = canonical_url.split("/")[-2]
                if not slug:
                    raise ValueError(f"Invalid value for slug: {slug}")
                return slug

    def _find_port(self) -> str:
        port = ""
        with open(self._output_filepath) as fin:
            for line in fin.readlines():
                # "\\d+" is the port number
                url = re.search(f"{self._local_domain}:\\d+", line)
                if url is None:
                    continue
                _, port = url.group().split(":")
                break
        return port

    def _md_filepath(self, html_filepath: str) -> str:
        basename = html_filepath.split(os.sep)[-1]
        basename = basename.replace(".html", ".md")
        return self._build_dir + basename

    def _to_md(self) -> None:
        with open(self._output_filepath, "w") as fout:
            with open(self._input_filepath) as fin:
                html_string = fin.readlines()
                html_string = "".join(html_string)
                md_string = md(html_string)
                fout.write(md_string)


if __name__ == "__main__":
    crosspost = Crosspost()
    crosspost.iter_md()
