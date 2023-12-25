import os

from PIL import Image, ImageDraw, ImageFont, ImageOps

from .enums import FooterIcon, HeaderIcon


class XmasGenerator:
    def __init__(
        self,
        text_color: str,
        border_color: str,
        canvas_color: str,
        header_icon: HeaderIcon,
        receiver: str,
        gifter: str,
        footer_icon: FooterIcon,
        output_file: str,
        assets_dir: str = 'assets',
        fonts_dir: str = 'fonts',
    ) -> None:
        self._text_color = text_color

        self._receiver = receiver
        self._gifter = gifter

        self._header_icon = header_icon
        self._footer_icon = footer_icon

        self._output_file = output_file

        self._assets_dir = assets_dir
        self._fonts_dir = fonts_dir

        self._font = ImageFont.truetype(os.path.join(self._fonts_dir, 'spline_sans_mono.ttf'), 13)
        self._image = ImageOps.expand(Image.new('RGBA', (250, 400), canvas_color), border=4, fill=border_color)

        self._draw = ImageDraw.Draw(self._image)

        self._header_map = {
            HeaderIcon.hat: self._draw_hat,
            HeaderIcon.tree: self._draw_tree,
            HeaderIcon.bell: self._draw_bell,
            HeaderIcon.grinch: self._draw_grinch,
            HeaderIcon.gift: self._draw_gift,
            HeaderIcon.door_deco: self._draw_door_deco,
        }

        self._footer_map = {
            FooterIcon.ribbon: self._draw_ribbon,
            FooterIcon.deer: self._draw_deer,
            FooterIcon.candy: self._draw_candy,
        }

    def _draw_hat(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, HeaderIcon.hat))
        icon = icon.resize((60, 60))
        self._image.paste(icon, (102, 20), icon)

    def _draw_tree(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, HeaderIcon.tree))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 20), icon)

    def _draw_bell(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, HeaderIcon.bell))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 20), icon)

    def _draw_grinch(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, HeaderIcon.grinch))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 20), icon)

    def _draw_gift(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, HeaderIcon.gift))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 20), icon)

    def _draw_door_deco(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, HeaderIcon.door_deco))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 20), icon)

    def _draw_header(self) -> None:
        self._header_map[self._header_icon]()
        msg = f'Dear {self._receiver}'

        self._draw.text((25, 120), msg, self._text_color, font=self._font)

    def _draw_body(self) -> None:
        msg = '''\n
They say
the best Christmas gifts
come from the heart …
but cash and gift cards
do wonders too!
Merry Christmas!

'''

        self._draw.text((40, 120), msg, self._text_color, font=self._font)

    def _draw_ribbon(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, FooterIcon.ribbon))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 300), icon)

    def _draw_deer(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, FooterIcon.deer))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 300), icon)

    def _draw_candy(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, FooterIcon.candy))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 300), icon)

    def _draw_footer(self) -> None:
        msg = f'From {self._gifter}'
        self._draw.text((25, 280), msg, self._text_color, font=self._font)
        self._footer_map[self._footer_icon]()

    def draw(self) -> None:
        self._draw_header()
        self._draw_body()
        self._draw_footer()

        self._image.save(f'{self._output_file}.png', format='png')
