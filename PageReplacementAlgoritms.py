# Author: Mehdi Lerari
# email: contactmehdilerari@gmail.com

from tkinter import Tk,Button
from random import randrange

FRAME_NUMBER = 4 
REFERENCE_CHAIN_LENGTH = 13

def FIFO():
    current_memory_state = []
    pageArrivingOrder = []
    global buttons
    for i in range(1,REFERENCE_CHAIN_LENGTH+1):
        
        for j in range(len(current_memory_state)):
            buttons[j+1][i].config(text=current_memory_state[j])    
        
        if (buttons[0][i]['text'] not in current_memory_state):
            if(len(current_memory_state)<FRAME_NUMBER):
                newPage = buttons[0][i]['text']
                pageArrivingOrder.append(newPage)
                current_memory_state.append(newPage)
                buttons[len(current_memory_state)][i].config(text=newPage)
            else:
                    newPage = buttons[0][i]['text'] 
                    indexOfPageToReplace = current_memory_state.index(pageArrivingOrder[0])
                    pageArrivingOrder.remove(pageArrivingOrder[0])
                    pageArrivingOrder.append(newPage)
                    current_memory_state[indexOfPageToReplace]=newPage 
                    buttons[indexOfPageToReplace+1][i].config(text=newPage)

def LRU():
    current_memory_state = [] 
    pageArrivingOrder = []
    global buttons
    for i in range(1,REFERENCE_CHAIN_LENGTH+1):
        
        for j in range(len(current_memory_state)):
            buttons[j+1][i].config(text=current_memory_state[j])    
        
        if (buttons[0][i]['text'] not in current_memory_state): 
            if(len(current_memory_state)<FRAME_NUMBER): 
                newPage = buttons[0][i]['text']
                pageArrivingOrder.append(newPage)
                current_memory_state.append(newPage)
                buttons[len(current_memory_state)][i].config(text=newPage)
            else: 
                    newPage = buttons[0][i]['text'] 
                    indexOfPageToReplace = current_memory_state.index(pageArrivingOrder[0])
                    pageArrivingOrder.remove(pageArrivingOrder[0])
                    pageArrivingOrder.append(newPage) 
                    current_memory_state[indexOfPageToReplace]=newPage 
                    buttons[indexOfPageToReplace+1][i].config(text=newPage)
        else: 
            pageArrivingOrder.remove(buttons[0][i]['text'])
            pageArrivingOrder.append(buttons[0][i]['text'])


def OPTIMAL():
    global buttons
    current_memory_state = [] 
    referenceChain = []
    turn = 0
    
    for i in range(1,REFERENCE_CHAIN_LENGTH+1):
        referenceChain.append(buttons[0][i]['text'])
    
    for i in range(1,REFERENCE_CHAIN_LENGTH+1):
        
        for j in range(len(current_memory_state)):
            buttons[j+1][i].config(text=current_memory_state[j])    
        
        if (buttons[0][i]['text'] not in current_memory_state): 
            if(len(current_memory_state)<FRAME_NUMBER): 
                newPage = buttons[0][i]['text']
                current_memory_state.append(newPage)
                buttons[len(current_memory_state)][i].config(text=newPage)
            else: 
                
                
                orderedList = []
                orderedList2 = []
                for k in range(i+1,REFERENCE_CHAIN_LENGTH+1):
                        if (buttons[0][k]['text'] in current_memory_state)and (buttons[0][k]['text'] not in orderedList) :
                            orderedList.append(buttons[0][k]['text'])
                for l in range(len(current_memory_state)):
                    if current_memory_state[l] not in orderedList:
                        orderedList2.append(current_memory_state[l])
                
                newPage = buttons[0][i]['text']
                if len(orderedList)==0:
                    
                    indexOfPageToReplace = current_memory_state.index(orderedList2[0])
                else:
                    indexOfPageToReplace = current_memory_state.index(orderedList[len(orderedList)-1])
                current_memory_state[indexOfPageToReplace]=newPage 
                buttons[indexOfPageToReplace+1][i].config(text=newPage)

def RESET():
    global buttons
    for i in range(1,REFERENCE_CHAIN_LENGTH+1):
        buttons[0][i].config(text=randrange(100),bg="grey")
        for j in range(1,FRAME_NUMBER+1):
            buttons[j][i].config(text="")

if __name__ == "__main__":
    mywindow = Tk()
    mywindow.title("Page replacement algorithms")
    buttons = []
    for ligne in range(FRAME_NUMBER+1):
        button_row = []
        for colonne in range(REFERENCE_CHAIN_LENGTH+1):
            button = Button(mywindow,borderwidth=1,width=7)
            button.grid(row=ligne, column=colonne)
            button_row.append(button)
        buttons.append(button_row)
    buttons[0][0].config(text="Frame/Page",bg="grey")
    lruButton=Button(mywindow,text="LRU", command=LRU,width=7,bg="grey")
    lruButton.grid(row=FRAME_NUMBER+3, column=0)
    fifoButton=Button(mywindow,text="FIFO", command=FIFO,width=7,bg="grey")
    fifoButton.grid(row=FRAME_NUMBER+3, column=1)
    optimalButton=Button(mywindow,text="Optimal", command=OPTIMAL,width=7,bg="grey")
    optimalButton.grid(row=FRAME_NUMBER+3, column=2)
    resetButton=Button(mywindow,text="Réinitialiser", command=RESET,width=7,bg="grey")
    resetButton.grid(row=FRAME_NUMBER+3, column=3)
    for i in range(1,FRAME_NUMBER+1):
        buttons[i][0].config(text=str(i),bg="grey")
    RESET()
    mywindow.mainloop()