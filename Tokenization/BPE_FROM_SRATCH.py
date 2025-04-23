from dataclasses import dataclass
from collections import defaultdict


class Tokenizer():
    """Abstract interface for a tokenizer
    """
    def encode(self,string:str)-> list[int]:
        raise NotImplementedError
    def decode(self,indices:list[int])->str:
        raise NotImplementedError


@dataclass(frozen=True)
class BPETokenizerParams:
    """Parameters for the BPE tokenizer."""
    vocab: dict[int,bytes]
    merges:dict[tuple[int,int],int]


class CharacterTokenizer(Tokenizer):
    """Tokenizer that splits the input string into individual characters"""
    def encode(self,string:str)-> list[int]:
        return list(map(ord,string))
    def decode(self,indices:list[int])->str:
        return ''.join(chr(i) for i in indices)

class ByteTokenizer(Tokenizer):
    """Represent a string  as a Sequence of bytes."""

    def encode(self,string: str) ->list[int]:
        string_bytes=string.encode("utf-8")
        indices =list(map(int,string_bytes))
        return indices
    def decode (self,indices: list[int]) -> str:
        string_btyes=bytes(indices)
        string=string_btyes.decode("utf-8")
        return string
    

def merge(indices: list[int], pair: tuple[int,int],new_index:int ) -> list[int]:
     

    new_indices=[]
    i=0
    while i<len(indices):
        if i+1<len(indices) and indices[i]==pair[0] and indices[i+1]==pair[1]:
            new_indices.append(new_index)
            i+=2
        else:
            new_indices.append(indices[i])
    return new_indices


class BPETokenizer(Tokenizer):
     """BPE tokenizer given a set of merges and a vocabulary."""
     def __init__(self,params: BPETokenizerParams):
         self.params=params
     def encode(self, string: str)-> list[int]:
         indices=list(map(int,string.encode("utf-8")))
         for pair,new_index in self.params.merges.items():
                indices=merge(indices,pair,new_index)
         return indices
     def decode(self, indices: list[int]) -> str:
         byte_list=list(map(self.params.vocab.get,indices))
         string=b"".join(byte_list).decode("utf-8")
         return string
     

def train_bpe(string: str, num_merges: int) -> BPETokenizerParams:
    ## start with list list of btyes of string.
    indices=list(map(int,string.encode("utf-8")))
    mereges: dict[tuple[int,int],int]={}
    vocab: dict[int,bytes]={x: bytes([x]) for x in range(256)}

    for i in range(num_merges):
        ## Count the number of Occurences of each pair of tokens
        counts=defaultdict(int)
        for index1,index2 in zip(indices,indices[1:]):
            counts[(index1,index2)]+=1
        
        ## Find the Most Common Pair
        pair=max(counts,key=counts.get)
        index1,index2=pair

        ## Merge that Pair
        new_index=256+i
        mereges[pair]=new_index
        vocab[new_index]=vocab[index1]+vocab[index2]
        indices=mereges(indices,pair,new_index)
    return BPETokenizerParams(vocab=vocab,merges=mereges)
