# -*- coding: utf-8 -*-

from git import Repo


class SimVer:
    path: str
    repo: Repo

    def __init__(self, params: dict):
        self.path = params['path']

    def main(self):
        self.repo = Repo(self.path)
        print(self.get_version())

    def get_version(self):
        tags = self.repo.tags
        tags.reverse()

        # there are no any tags
        if not tags:
            return str(self.repo.head.commit)

        last_tag = tags[0]

        # we are exactly checked out at the TAG
        if last_tag.commit == self.repo.head.commit:
            return str(last_tag)

        return str(last_tag) + "+" + str(self.repo.head.commit)
