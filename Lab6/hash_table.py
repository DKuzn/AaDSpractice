from dataclasses import dataclass
from typing import List


@dataclass
class TInfo:
    phone: str = " "
    name: str = " "


@dataclass
class THashItem:
    info: TInfo
    empty: bool = True
    visit: bool = False


@dataclass
class HashItemChain:
    info: TInfo
    del_info = False


class MyHash:
    hash_table: List[HashItemChain]
    info: TInfo

    def __init__(self, size_table):
        self.size_table = size_table
        self.info = TInfo()
        self.hash_table = [HashItemChain(info=self.info) for _ in range(self.size_table)]
        self.size = 0
        self.step = 37

    def __hash_function(self, s):
        result = 0
        for i in range(len(s)):
            result += int(s[i]) * i
            result //= self.size_table
        return result

    def add_hash(self, name: str, phone: str):
        adr = -1
        if self.size < self.size_table:
            adr = self.__hash_function(phone)
            while not self.hash_table[adr].empty:
                adr = (adr + self.step) // self.size_table
            self.hash_table[adr].empty = False
            self.hash_table[adr].visit = True
            self.hash_table[adr].info.name = name
            self.hash_table[adr].info.phone = phone
            self.size += 1
        return adr

    def __clear_visit(self):
        for i in self.hash_table:
            i.visit = False

    def find_hash(self, phone: str):
        result = -1
        ok: bool
        name = " "
        count = 1
        self.__clear_visit()
        i = self.__hash_function(phone)
        ok = self.hash_table[i].info.phone == phone
        while not ok and not self.hash_table[i].visit:
            count += 1
            self.hash_table[i].visit = True
            i = (i + self.step) // self.size_table
            ok = self.hash_table[i].info.phone == phone
        if ok:
            result = i
            name = self.hash_table[i].info.name
        return result

    def del_hash(self, phone: str):
        result = False
        i = 0
        if self.size != 0:
            i = self.__hash_function(phone)
            if self.hash_table[i].info.phone == phone:
                self.hash_table[i].empty = True
                result = True
                self.size -= 1
            else:
                i = self.find_hash(phone)
                if (i != -1):
                    self.hash_table[i].empty = True
                    result = True
                    self.size -= 1
        return result

    def __str__(self):
        out_list = []
        if self.hash_table[0] is not None:
            for i in range(len(self.hash_table)):
                out = "i + 1" + " " + self.hash_table[i].phone + " " + self.hash_table[i].name
                out_list.append(out)
        return out_list
