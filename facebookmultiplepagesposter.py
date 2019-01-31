
import facebook

# Write here the names of the pages you don't want to post to
BLACKLIST = []

# Write here the link you want to share
LINK = ""

# Paste here your Access Token with perision to manage and post on pages
ACCSESSTOKEN = ""


def main():
    api = get_api()


def get_api():

    # Accesses data on the user's pages where he is admin
    graph = facebook.GraphAPI(ACCSESSTOKEN)
    resp = graph.get_object('me/accounts?limit=200')
    infor = resp['data']

    # Makes an ordered list with all the pages names, tokens, and ids
    pages = []
    for page in infor:
        pages.append([page['name'], page['access_token'], page['id']])

    pages.sort()

    # Posts on each page
    if input(f"Are you sure you want to post {LINK} on {len(pages)-len(BLACKLIST)} pages? ") == 'y':

        count = 0
        for page in pages:
            if not page[0] in BLACKLIST:
                pgraph = facebook.GraphAPI(page[1])
                pgraph.put_object(parent_object=page[2], connection_name='feed', link=LINK)
                print(f"Posted on {page[0]}")
                count += 1

        print(f"posted in {count} out of {len(pages)-len(BLACKLIST)} pages")


if __name__ == '__main__':
    main()
