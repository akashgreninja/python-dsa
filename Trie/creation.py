


class TrieStruct:
    def __init__(self):
        self.endOfString=False
        self.childern={}

class Trie:
    def __init__(self):
        self.root=TrieStruct()

    def insert(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.childern.get(ch)
            if node==None:
                node=TrieStruct()
                current.childern.update({ch:node})
            current =node
        
        current.endOfString=True
        print("sucessfullty inserted")

    def SearchString(self,word):
        curNode=self.root
        for i in word:
            node=curNode.childern.get(i)
            if node==None:
                return False
            curNode=node
        
        if curNode.endOfString==True:
            return True
        else:
            return False



def deleteString(root,word ,index):
    ch=word[index]
    curNode=root.childern.get(ch)
    canbedeleted=False

    if len(curNode.childern  )>1:
        deleteString(curNode,word,index+1)
        return False
    
    if index==len(word)-1:
        if len(curNode.childern)>=1:
            curNode.endOfString=False
            return False
        else:
            root.childern.pop(ch)
            return True

    if curNode.endOfString==True:
        deleteString(curNode,word,index+1)
        return False
    canbedeleted=deleteString(curNode,word,index+1)
    if canbedeleted==True:
        root.childern.pop(ch)
        return True
    else:
        return False


newRoot=Trie()
newRoot.insert("App")
newRoot.insert("AppL")
deleteString(newRoot.root,"App",0)

print(newRoot.SearchString("App"))