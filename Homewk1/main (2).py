def typeBasedTransformer(**kwargs):

    for type1, final in kwargs.items():
        
        if isinstance(final, bool):
            ans_final = not final
        
        elif isinstance(final, (int, float)):
            ans_final = final ** 2
        
            
        elif isinstance(final, str):
            ans_final = final[::-1]
            
        elif isinstance(final, (list, tuple)):
            ans_final = final[::-1]
            
        elif isinstance(final, dict):
            ans_final = {a: b for b, a in final.items()}
            
        else:
            ans_final = final


        print(f"{type1} = {ans_final}") 


typeBasedTransformer(
    
    power = 2,
    TF=True,
    word = "Code is working",
    lt = [1, 3, 5,],
    mix = {"final": 0, "power": 100},
     
)