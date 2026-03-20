"""Created on 20260311_1130"""
import hashlib

class MyersBriggsUtil:
    """
    The utility class for the MyersBriggs* related objects.
    """
    @staticmethod
    def global_hash(seed : str, hashfunction : str, encoding : str = "utf-8"):
        """
        The function returns the hash result for a given seed string and hash function.
        """
        if hashfunction is None:
            return
        if seed is None:
            return
        
        hashresult = seed
        encoded_seed = seed.encode(encoding)

        match hashfunction.lower():
            case 'sha-1':
                m = hashlib.sha1()
                m.update(encoded_seed)
                hashresult = m.hexdigest()
        
        return hashresult
    
    @staticmethod
    def isListSameType( somelist : list, sometype : type) -> bool:
        """
        The function determines if all the objects in the list have the exact same type,
        i.e. int, str, of an object certain class.
        """        
        if len(somelist) > 0:
            return all(isinstance(x, sometype) for x in somelist)
        
        return True
    
    @staticmethod
    def __main_demo__():
        """
        This function demonstrates the call to several utlity functions:
        isListSameType
        global_hash
        """
        print(MyersBriggsUtil.isListSameType([10, '10'], list))
        print(MyersBriggsUtil.isListSameType([10, 10], int))
        print(MyersBriggsUtil.isListSameType([10, '10'], str))
        print(MyersBriggsUtil.isListSameType(['20', '10'], str))

        print(MyersBriggsUtil.global_hash('ENTF','sha-1'))


if __name__ == "__main__":
    MyersBriggsUtil.__main_demo__()
