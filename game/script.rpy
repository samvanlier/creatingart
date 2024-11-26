image movie = Movie(
    "./video/workstation line-art.webm",
    size=(6444, 2900),
    yanchor='center',
    ypos= .5,
    play="./video/workstation line-art.webm",
    image="./images/backgrounds/bg workstation line-art.png",
    loop=False
)
label start:

    "lets start this drawing!!!!"

    # show movie with fade

    $renpy.movie_cutscene("./video/workstation line-art.webm")
    
    show bg workstation line-art
    with dissolve

    "hello"

    "this is a test"

    return
