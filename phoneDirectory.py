#Design a Phone Directory which supports the following operations:

#get: Provide a number which is not assigned to anyone.
# availDirectory = { '408': set('0000000', '0000001') }

#check: Check if a number is available or not.
# check 408 000 0003
# if '408' in availDirectory:
#    if '0000003' in availDirectory['408']

#release: Recycle or release a number.
# usedDirectory

#search:Number based on the input
# 408 000 0003
# 408


# 408 001 0003. 408 002 0003
# 408 => [408 0001 0003,408 002 0003]
# 40
# availDirectory = { '4': { '0': { '8'

class Node(object):
    def __init__(self, val):
        self.children = {}
        self.val = val
        self.end = False

class PhoneDirectory(object):
    def __init__(self):
        self.avail = 0 #representing 000 000 0000
        self.lookupDir = set()
        self.released = set()
        self.root = Node(0)
        
    # check max num didnt overflow
    def get(self):
        number = None
        if self.released:
            number = self.released.pop()
        else:
            num = self.avail
            phoneNum = [0] * 10
            for i, c in enumerate(str(num)[::-1]):
                phoneNum[-1-i] = int(c)
            self.avail += 1
            number = ''.join(map(str, phoneNum))
        self.lookupDir.add(number)
        self.addToSearch(number)
        return number
        
    def check(self, number):
        if number in self.lookupDir:
            return False
        else:
            return True
        
    def release(self, number):
        if number in self.lookupDir:
            self.lookupDir.remove(number)
            self.released.add(number)
      
    def addToSearch(self, number):
        node = self.root
        for c in number:
            if c not in node.children:
                node.children[c] = Node(c)   
            node = node.children[c]
        node.end = True
        
    def dfs(self, node, nums, res):
        if node:
            nums.append(node.val)
            if node.end:
                res.append(''.join(nums))
                nums.pop()
            else:     
                for key in node.children:
                    self.dfs(node.children[key], nums, res)
        
    def search(self, number):
        node = self.root
        nums = []
        for c in number:
            if c not in node.children:
                return []
            nums.append(c)
            node = node.children[c]
        res = []
        self.dfs(node, nums, res)
        return res

    
    

pd = PhoneDirectory()
nums = []
for i in range(10):
    number = pd.get()
    nums.append(number)
# nums[1] == 000 000 0001
print nums
print pd.check(nums[1]) == False
pd.release(nums[1])
print pd.check(nums[1]) == True
print pd.check('4080000003') == True

#0000000007
print pd.check('0000000007')
pd.release('0000000007')
print pd.check('0000000007')

print pd.search('000')
