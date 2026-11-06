import webbrowser

try:
    webbrowsr.open("https://www.youtube.com")
    if TypeError:
        print("A TypeError occurred while trying to open the web browser.")

except BaseException as e:
    print("An error occurred while trying to open the web browser:", e) 

finally:
    print("This is parsed as 'finally' statement.")


# BaseException












