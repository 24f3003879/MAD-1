import pyhtml as ht
t = ht.html(
    ht.head(
        
    ),
    ht.body(
        ht.h1("Heading 1"),
        ht.em("My name is ram"),
        ht.strong("Bold"),
        ht.div(
            ht.h2("Heading 2"),
            ht.div("This is the nested div section")
            
        ),
        ht.div(
            ht.h3(
                "Heading 3"
            ),
            ht.p(
                "This is a paragraph"
            )
        )
        
        
    )
    
    

)

print(t.render())