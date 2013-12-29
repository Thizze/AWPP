import sfml as sf

mwindow = sf.RenderWindow(sf.VideoMode(640, 480), "SFML Application")
mplayer = sf.CircleShape()

class myclass:
    mplayer.radius = 40
    mplayer.position = (100, 100)
    mplayer.fill_color = sf.Color.CYAN

    def run(self):
        while mwindow.is_open:
            myclass.processevents(self)
            myclass.update(self)
            myclass.render(self)

    def processevents(self):
        event = sf.Event
        for event in mwindow.events:
            if type(event) is sf.CloseEvent:
                mwindow.close()

    def update(self):
        pass

    def render(self):
        mwindow.clear()
        mwindow.draw(mplayer)
        mwindow.display()