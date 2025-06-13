import requests
from bs4 import BeautifulSoup


class wikiReferenceScraper(object):
    def get_page_url(url):
        page = requests.get(url)
        if page.status_code == 200:
            return page.text
        else:
            print("Check the url entered")

    def get_references(self, url):
        """
        This function calls the get_url_page() function.
        The response from the get_url_page() function is parsed as html.
        :param url: This is the url of the page that is to be scrapped
        :return: The return object is an html object
        """
        page_text = self.get_url_page(url)
        soup = BeautifulSoup(page_text, "html.parser")
        citations = soup.find_all("cite")
        return citations

    def write_to_document(self, url, document_name):
        """
        This is the main fucntion that calls the above fucntions and then does the actual write to
        document.
        :param url: This is the url of the page that is to be scrapped
        :param document_name: The name of the document that our scrapped data will be written to
        :return: There is no return object
        """
        with open(document_name, "w") as file:
            for citation in self.get_references(url):
                file.write("\n\n")
                for string in citation.strings:
                    file.write(string)


if __name__ == "__main__":
    wikiReferenceScraper.get_page_url(
        "https://en.wikipedia.org/wiki/Blood_pressure#References"
    )
    wikiReferenceScraper.get_references(
        "https://en.wikipedia.org/wiki/Blood_pressure#References"
    )
    wikiReferenceScraper.write_to_document(
        "https://en.wikipedia.org/wiki/Blood_pressure#References", "TestDoc"
    )
