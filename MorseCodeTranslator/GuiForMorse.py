import tkinter as tk
import MorseTranslator

root = tk.Tk()

root.geometry("600x300")
# string variables for storing
msg_var = tk.StringVar()
morse_var = tk.StringVar()


def Encrypt():
    msg = msg_entry.get()
    msg.upper()
    cipher = MorseTranslator.encrypt(msg)
    # print(cipher)
    msg_ans.config(text=cipher,font=('calibre', 20, 'bold'))


def Decrypt():
    morse = morse_entry.get()
    dec = MorseTranslator.decrypt(morse)
    morse_ans.config(text=dec,font=('calibre', 15, 'bold'))
    # print(dec)


# Head label
head = tk.Label(root, text="Note:Use Capital letters for ease of use  ", font=('calibre', 10, 'bold'))
# Message labels
msg_label = tk.Label(root, text="Message", font=('calibre', 15, 'bold'))
msg_ans = tk.Label(root, text="Here is the Morse Code for your Message", font=('calibre', 13, 'bold'))

# Message input entry
msg_entry = tk.Entry(root, textvariable=msg_var, font=('calibre', 15, 'bold'))

# morse labels

morse_label = tk.Label(root, text='Morse Code', font=('calibre', 15, 'bold'))
morse_ans = tk.Label(root, text='Here is the Text for your MorseCode', font=('calibre', 13, 'bold'))

# creating entry for morse
morse_entry = tk.Entry(root, textvariable=morse_var, font=('calibre', 15, 'normal'))

# Encrypt button
enc_btn = tk.Button(root, text='Encrypt', command=Encrypt)

# Decrypt button
dec_btn = tk.Button(root, text='Decrypt', command=Decrypt)

# placing the label and entry in
# the required position using grid  method
head.grid(row=2, column=3)
msg_label.grid(row=3, column=2)
msg_entry.grid(row=3, column=3)
msg_ans.grid(row=4, column=3)
enc_btn.grid(row=5, column=3)
morse_label.grid(row=6, column=2)
morse_entry.grid(row=6, column=3)
morse_ans.grid(row=7, column=3)
dec_btn.grid(row=8, column=3)

root.mainloop()
