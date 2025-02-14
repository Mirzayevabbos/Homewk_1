def kwargsAcceptFun(**kwargs):

    for word, inf in kwargs.items():
        
        print(f"{word} - {inf}")

kwargsAcceptFun( Name= "Ali", Age="21", Status= "Single" )