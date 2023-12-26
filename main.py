from app.generator import FooterIcon, HeaderIcon, XmasGenerator

if __name__ == '__main__':
    text_color = input('Enter text color [default == \'white\']:\n').strip() or 'white'
    border_color = input('Enter border color [default == \'red\']:\n').strip() or 'red'
    canvas_color = input('Enter canvas color [default == \'green\']:\n').strip() or 'green'
    gifter = input("Enter gifter name [default == \'Anonymous\']:\n") or 'Anonymous'
    receiver = input('Enter name of the receiver [default == \'Grinch\']:\n').strip() or 'Grinch'
    output_file = input("enter output file name [default == \'card\']: \n").strip() or 'card'

    header_icons = '''
  1)Grinch [default]
  2)Santa Hat
  3)Xmas Tree
  4)Bell
  5)Gift
  6)Xmas Door Deco
  '''

    header_map = {
        '1': HeaderIcon.grinch,
        '2': HeaderIcon.hat,
        '3': HeaderIcon.tree,
        '4': HeaderIcon.bell,
        '5': HeaderIcon.gift,
        '6': HeaderIcon.door_deco,
    }
    while True:
        try:
            hic = input(f'Enter ICON for header\nAvailable Icons\n {header_icons} Enter option : ').strip() or '1'
            header_icon = header_map[hic]
        except KeyError:
            print('No valid option found. Please retry')  # noqa
        else:
            break

    footer_icons = '''
    1)Anonymous [default]
    2)Deer
    3)Ribbon
    4)Candy

  '''

    footer_map = {
        '1': FooterIcon.anonymous,
        '2': FooterIcon.deer,
        '3': FooterIcon.ribbon,
        '4': FooterIcon.candy,
    }

    footer_icon = None
    while True:
        try:
            fic = input(f'Enter ICON for footer\nAvailable Icons\n {footer_icons} Enter option : ').strip() or '1'
            footer_icon = footer_map[fic]
        except KeyError:
            print('No valid option found. Please retry')  # noqa
        else:
            break

    xmas_gen = XmasGenerator(
        text_color, border_color, canvas_color, header_icon, receiver, gifter, footer_icon, output_file
    )
    xmas_gen.draw()
