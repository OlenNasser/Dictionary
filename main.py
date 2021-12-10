import PySimpleGUI as sg
from PyDictionary import PyDictionary
dic = PyDictionary()

class MAIN:
    def __init__(self):
        self.gui = GUI()
        pass
    def main(self):
        self.gui.main()
        pass
class GUI:
    def __init__(self):
        self.n = 1
        self.definition = " "
        self.synonym = " "
        self.antonym = " "
        sg.theme('DarkAmber') #theme dumbass
        self.layout = [
            [sg.Text(size = 15), sg.Text("oBoonkero's Dictionary", font = 'acme 50')],


            [sg.Text("Enter Word:")],
            
            
            [sg.InputText(), sg.Button('Search')],


            [sg.Text("Definition:", size = (40, 1)), sg.Text("Synonym", size = (40, 1)), sg.Text("Antonym", size = (40, 1))],
            
            # Mutliline = Text but with scrolly
            [sg.Multiline(" ", size = (40, 10), key = "meaning"), 
            sg.Multiline(" ", size = (40, 10), key = "synonym"),
            sg.Multiline(" ", size = (40, 10), key = "antonym")]
        ]
        self.window = sg.Window("Oboonkero's Dictionary", self.layout, icon = "Henry_V_England.ico")
        pass
    def main(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Search':
                meaning = dic.meaning(values[0])
                if meaning == None:
                    meaning = "No definition found"
                self.window['meaning'].update(value = meaning)
                
                self.synoym = dic.synonym(values[0])
                if self.synoym == None:
                    self.synoym = "No synonym found"
                self.window['synonym'].update(value = self.synoym)

                self.antonym = dic.antonym(values[0])
                if self.antonym == None:
                    self.antonym = "No antonym found"
                self.window['antonym'].update(value = self.antonym)
                pass
            

main = MAIN()

main.main()