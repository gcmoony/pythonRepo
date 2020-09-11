import tkinter as tk

####
version = 0.01
####

class CsvWindow:
    

    def __init__(self):
        # Window Setup
        self.window = tk.Tk()
        self.window.title(f"Dynamic CSV {version}")
        self.rows = 0
        self.cols = 1

        # Navigation Bar Setup
        self.addButton(self.window, "Open File..").grid(row = 0, column = 0, sticky = "n")
        self.addButton(self.window, "New CSV").grid(row = 1, column = 0, sticky = "n")

        # Content Controls Setup
        self.contentControls = self.addFrame()
        tk.Label(self.contentControls, text = "Rows", padx = 2).grid(row = 0, column = 1)
        self.addButton(self.contentControls, "-", buttonLen= 1, aCommand= lambda: self.entryFrame.grid_slaves()[0].destroy()).grid(row = 0, column = 0)
        self.addButton(self.contentControls, "+", buttonLen= 1, aCommand= lambda: self.addRow(self.entryFrame)).grid(row = 0, column = 2)

        tk.Label(self.contentControls, text = "Columns", padx = 2).grid(row = 0, column = 4)
        self.addButton(self.contentControls, "-", buttonLen= 1, aCommand=lambda: self.printSlaves(self.entryFrame)).grid(row = 0, column = 3)
        self.addButton(self.contentControls, "+", buttonLen= 1, aCommand=lambda: self.addCol(self.entryFrame)).grid(row = 0, column = 5)

        # Entry Frame Setup
        self.entryFrame = self.addFrame()

        # Geometry Setup
        #self.navBar.grid(row = 0, column = 0, padx = 10)
        self.contentControls.grid(row = 0, column = 1, sticky = "n")
        self.entryFrame.grid(row = 1, column = 1, sticky = "n")
        
        # Start
        self.window.mainloop()


    def addFrame(self):
        newFrame = tk.Frame(
            self.window
        )
        return newFrame


    @staticmethod
    def addButton(aFrame, buttonText, aCommand = None, buttonLen = 12, buttonHeight = 1):
        newButton = tk.Button(
            aFrame,
            text = buttonText,
            width = buttonLen,
            height = buttonHeight,
            command = aCommand
        )
        return newButton


    def addRow(self, aFrame):
        newRow = tk.Entry(
            aFrame
        )
        newRow.grid(row = self.rows, sticky = "nw")
        self.rows += 1

    def addCol(self, aFrame):
        for row, rowFrame in enumerate(aFrame.grid_slaves()):
            newCol = tk.Entry(
                rowFrame
            )
            newCol.grid(row = row, column = self.cols)
        self.cols += 1


    @staticmethod
    def printSlaves(aFrame):
        print(aFrame.grid_slaves())
        for row, items in enumerate(aFrame.grid_slaves()):
            print(f"Row {row}: {items}")


def main():
    CsvWindow()


if __name__ == '__main__':
    main()