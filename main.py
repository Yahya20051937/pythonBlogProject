import logging
import tkinter

from posts_management.post_interactions import add_comment, add_comment_async, add_like, add_like_async
from posts_management.gui_interactions import interact_gui
from Flask.app import Flask__

if __name__ == '__main__':
    pass
    # Flask__.run()

logging.basicConfig(format='%(asctime)s %(levelname)-8s[%(filename)s:%(lineno)d] %(message)s', datefmt='%d-%m-%Y '
                                                                                                       '%H:%M:%S ',
                    level=logging.DEBUG,
                    filename='logs1.txt1')
logger = logging.getLogger('logs')

# logging.disable(logging.DEBUG)


func = add_comment_async(add_comment())
func.send(None)

func2 = add_like_async(add_like())
func2.send(None)

interact_gui('yahya_05', 100, root=tkinter.Tk())

