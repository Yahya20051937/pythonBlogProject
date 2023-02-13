import tkinter as tk
import queue
from tkinter import ttk


def comment_on_post_gui():
    from posts_management.post_interactions import q1, q, q2, q3, get_comments_users, send_data
    from main import func, logger

    user_name, post_id, root, frame = q1.get()
    print(user_name, post_id, root, frame)
    main_frame = tk.Frame(root)
    comments_data = get_comments_users(post_id)

    all_data_frame = tk.Frame(main_frame)
    all_data_frame.pack(side='top', fill='both', expand=True)
    logger.debug(f'comments data: {comments_data}')
    for comment in comments_data:
        f = tk.Frame(all_data_frame)
        f.pack(side='left', fill='x', expand=True)

        label1 = tk.Label(f, text=comment[0], borderwidth=1, relief='sunken')
        label1.pack(side='top')

        label2 = tk.Label(f, text=f'By {comment[1]}', font=('italic', 5))
        label2.pack(side='bottom')

    q3.put((user_name, post_id, root))
    frame.destroy()

    q2.put(main_frame)
    main_frame.pack(fill='both', expand=True)
    frame1 = ttk.Frame(main_frame)
    text_area = tk.Text(frame1)

    label = tk.Label(frame1, text='Enter your comment here:')

    frame1.pack(fill='both', expand=True)
    label.pack(side='top', fill='x', expand=True)
    text_area.pack(side='top', fill='both', expand=True)

    button3 = tk.Button(frame1, text='Go back to the page', command=restart)

    button = tk.Button(frame1, text='Submit',
                       command=lambda: send_data(user_name, post_id, text_area, button3, button, func=func))
    button.pack(side='bottom')

    q.put(frame1)
    # button.pack(side='bottom')


def interact_gui(user_name, post_id, root):
    from main import func2
    from posts_management.post_interactions import q2, q1, send_data

    i = None
    try:
        f = q2.get(timeout=0.2)
        f.destroy()
        i = 0
    except queue.Empty:
        i = 1

    frame = tk.Frame(root)
    frame1 = tk.Frame(frame)
    frame2 = tk.Frame(frame)
    q1.put((user_name, post_id, root, frame))
    liked_button = tk.Button(frame2, text='👍', background='blue', font='Black',
                             command=lambda: send_data(post_id, like_button, liked_button, frame2, func=func2))
    like_button = tk.Button(frame1, text='👍', background='white', font='Blue',
                            command=lambda: send_data(post_id, like_button, liked_button, frame2, func=func2))
    comment_button = tk.Button(frame1, text='✎', background='gray', font='Black', command=comment_on_post_gui)
    share_button = tk.Button(frame1, text='⤻', background='white', font='Black')

    frame.pack(fill='x', expand=True)
    frame1.pack(side='right', fill='x', expand=True)

    like_button.pack(side='left', fill='x', expand=True)
    comment_button.pack(side='left', fill='x', expand=True)
    share_button.pack(side='left', fill='x', expand=True)
    if i == 1:
        print(55)
        tk.mainloop()


def restart():
    from posts_management.post_interactions import q3
    username, post_id, root = q3.get()
    interact_gui(username, post_id, root)
