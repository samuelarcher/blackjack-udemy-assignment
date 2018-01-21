from SimpleGUI import SimpleGUI

sg = SimpleGUI

SimpleGUI.say("Saying something")
SimpleGUI.warn("This is a warning")
SimpleGUI.error("This is an error")

yesno = SimpleGUI.ask_yes_no("Yes or no?")
SimpleGUI.say("You input '{}'".format(yesno))

answer = SimpleGUI.ask_text_input("What's your input?")
SimpleGUI.say("You input '{}'".format(answer))