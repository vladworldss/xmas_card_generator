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

    def _draw_header(self) -> None:
        icon = Image.open(os.path.join(self._assets_dir, self._header_icon))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 20), icon)

        msg = f'Dear {self._receiver},'

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

    def _draw_footer(self) -> None:
        msg = f'From {self._gifter}'
        self._draw.text((25, 280), msg, self._text_color, font=self._font)

        icon = Image.open(os.path.join(self._assets_dir, self._footer_icon))
        icon = icon.resize((70, 70))
        self._image.paste(icon, (98, 300), icon)

    def draw(self) -> None:
        self._draw_header()
        self._draw_body()
        self._draw_footer()

        self._image.save(f'{self._output_file}.png', format='png')
