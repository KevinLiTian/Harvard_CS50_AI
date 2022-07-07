pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )