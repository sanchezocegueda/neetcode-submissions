class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.num_components = n

    def find(self, x: int) -> int:
        cur = x
        to_update = []
        while self.parent[cur] != cur:
            to_update.append(cur)
            cur = self.parent[cur]
        
        for u in to_update:
            self.parent[u] = cur

        return cur

    def union(self, x: int, y: int) -> bool:

        if self.isSameComponent(x, y):
            return False
        
        xRoot = self.find(x)
        yRoot = self.find(y)
        self.parent[xRoot] = yRoot
        self.num_components -= 1
        return True

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Step 1: setup
        # - figure out how many accounts there are
        # - create the union-find object

        id_count = 0
        ids = {} # id |-> emails
        id_to_name = {} # id |-> owner name
        emails_to_ids = {} # email |-> account ids

        for acc in accounts:
            name = acc[0]
            emails = acc[1:]
            ids[id_count] = set(emails)
            id_to_name[id_count] = name

            for email in emails:
                if email in emails_to_ids:
                    emails_to_ids[email].append(id_count)
                else:
                    emails_to_ids[email] = [id_count]
            id_count += 1
        
        print(ids)
        print(emails_to_ids)
        uf = UnionFind(id_count)


        # merge all accounts
        for email in emails_to_ids.keys():
            associated_ids = emails_to_ids[email]
            if len(associated_ids) > 1:
                first = associated_ids[0]
                for other_id in associated_ids[1:]:
                    uf.union(first, other_id)

        # add email to root component
        for email in emails_to_ids.keys():
            associated_id = emails_to_ids[email][0]
            root_id = uf.find(associated_id)

            ids[root_id].add(email) # make sure root id has that email in its list

            
        # consolidate into output
        output = []
        for i in range(id_count):
            if uf.find(i) == i: # i is a root
                name = id_to_name[i]
                account_emails = sorted(list(ids[i]))
                output.append([name] + account_emails)



        return output