import pyhtml as h

t = h.html(
    h.head(h.title("My title")),
    h.body(
        h.div(h.div(h.h2("inside title")), h.p("some text in a paragraph"))
    )
)

print(t.render())