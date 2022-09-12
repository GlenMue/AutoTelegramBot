from tkinter import*
from tkinter import scrolledtext
from urllib import request
import requests
from bs4 import BeautifulSoup as soup

root = Tk()

groups1 = ['hentai', 'romantic', 'slice of life']
groups2 = ['animezone', 'animix', 'toonimation']

url2 = 'https://web.telegram.org/k/'
page = requests.get(url2)
Soup = soup(page.content, 'html.parser')

# l = Soup.find_all("ul", class_='chatlist')
l = Soup.find_all(
    "div", class_='scrollable scrollable-y tabs-tab chatlist-parts active')

print(Soup.prettify())


def post():
    # follow video
    def send(message, group):
        ident = 'https://api.telegram.org/bot5482968451:AAHSv5OiQX0Eq8rGFf_hP3wVFdmOMosP-cE/getUpdates'

        print("{0} was sent to {1}".format(message, group))
        url = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(
            token.get(), '-778677888', message)
        requests.get(url)

    def get_groups():
        group_url = 'telegram website with to scrape the names of groups'

        # scrape the names of groups present
        print(groups1)
    popup = Toplevel()
    popup.title("Post")

    welcome = Label(popup,
                    text="Post whatever message or media here with the time they will be sent")
    welcome.pack()

    frame2 = Frame(popup, bg='skyblue', bd=3)
    frame2.pack()

    entry = scrolledtext.ScrolledText(frame2, wrap=WORD,
                                      width=40, height=8,
                                      font=("Times New Roman", 15))

    entry.grid(column=1, row=2, sticky=W, pady=10, padx=10)
    entry.focus()
    button = Button(frame2, text="Send",
                    command=lambda: send(entry.get('1.0', END), 'hello'))
    button.grid(column=2, row=2, sticky=S, pady=10,
                padx=10)

    # placing cursor in text area


def steal():
    # follow video on scraping telegram users
    def transfer_(group1, group2):
        print("group members of '{0}' where transfered to '{1}'").format(
            group1, group2)
    popup = Toplevel()
    popup.title("Steal")

    welcome = Label(popup,
                    text="Steal group members from a group and add to your group")
    welcome.pack()

    frame2 = Frame(popup, bg='skyblue', bd=3)
    frame2.pack()

    group1_ = Entry(frame2)
    group1_.grid(column=1, row=0)

    group1_ = StringVar(frame2)
    group1_.set((list(groups1))[0])

    x = OptionMenu(frame2, group1_, *(list(groups1)))
    x.grid(column=1, row=0)

    group2_ = Entry(frame2)
    group2_.grid(column=3, row=0)

    group2_ = StringVar(frame2)
    group2_.set((list(groups2))[0])
    y = OptionMenu(frame2, group2_, *(list(groups2)))
    y.grid(column=3, row=0)

    transfer = Button(frame2, text="Transfer", command=lambda: transfer_)
    transfer.grid(row=1, column=2)


def create(group):
    # idk, maybe last minute plan
    print("'{}' was created")

    popup = Toplevel()
    popup.title("Steal")

    welcome = Label(popup,
                    text="Write the name of the group to be created")
    welcome.pack()

    frame2 = Frame(popup, bg='skyblue', bd=3)
    frame2.pack()

    group1_ = Entry(frame2)
    group1_.grid(column=1, row=0)


canvas = Canvas(root)
canvas.pack()

intro_label = Label(
    canvas, text="Welcome!")
intro_label.pack()

frame1 = Frame(root, bg='skyblue', bd=3)
frame1.pack()

token_ = Label(frame1, text='Token')
token = Entry(frame1)
token_.pack()
token.pack()

frame = Frame(root, bg='skyblue', bd=3)
frame.pack()


post_button = Button(frame, text="Post",
                     command=lambda: post())
post_button.grid(row=1, column=1)

steal_button = Button(frame, text="Steal", command=lambda: steal())
steal_button.grid(row=1, column=3)

create_button = Button(frame, text="Create")
create_button.grid(row=2, column=2)

root.mainloop()
