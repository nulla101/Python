import justpy as jp


class Doc:

    def serve(self):
        wp = jp.WebPage()

        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

        jp.Div(a=div, text="Instant Dictionary API", classes="text-4xl text-center n-2 pt-8 pb-12")
        jp.Div(a=div, text="Get definition of words:", classes="text-lg font-bold")
        jp.Hr(a=div)
        jp.Div(a=div, text="www.example.com/api?w=house")
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "house", 
        "definition": 
        ["The abode of a human being, their place of residence.", 
        "To keep within a structure or container; to contain or cover.", 
        "A place that a human built to live in.", 
        "A place where an activity is accomplished, whether actual, as a pub, or virtual, as a website.", 
        "A familiar descendance, for example, a Royal House.", 
        "To admit to residence; provide housing for.", 
        "One of 12 equal areas into which the zodiac is divided."]}
        """)

        return wp

