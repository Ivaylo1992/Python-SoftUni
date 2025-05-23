from math import ceil

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.current_page = 0

    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return PhotoAlbum(pages)

    def add_photo(self, label: str) -> str:
        if len(self.photos[self.current_page]) == self.PHOTOS_PER_PAGE:
            self.current_page += 1

        if self.current_page >= len(self.photos):
            return "No more free slots"

        self.photos[self.current_page].append(label)

        return (f"{label} photo added successfully on page {self.current_page + 1}"
                f" slot {len(self.photos[self.current_page])}")

    def display(self) -> str:
        result = ['-----------']

        for page in range(len(self.photos)):
            photos = ''
            for _ in self.photos[page]:
                photos += '[] '
            result.append(photos.strip())
            result.append('-----------')

        return '\n'.join(result)