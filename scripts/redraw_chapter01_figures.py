from __future__ import annotations

import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


SITE = Path(__file__).resolve().parents[1]
ROOT = SITE.parent

OUT_NAME = "fig1-1_complexity_sources_native.png"
TARGETS = [
    ROOT / "textbook" / "figures_fixed" / "chapter01" / "student" / OUT_NAME,
    SITE / "assets" / "figures" / "textbook" / "chapter01" / "student" / OUT_NAME,
    SITE / "docs" / "assets" / "figures" / "textbook" / "chapter01" / "student" / OUT_NAME,
]

FONT_CANDIDATES = [
    Path("C:/Windows/Fonts/msyhbd.ttc"),
    Path("C:/Windows/Fonts/msyh.ttc"),
    Path("C:/Windows/Fonts/simhei.ttf"),
    Path("C:/Windows/Fonts/NotoSansSC-VF.ttf"),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = FONT_CANDIDATES if bold else FONT_CANDIDATES[1:] + FONT_CANDIDATES[:1]
    for path in candidates:
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        candidate = current + ch
        if text_size(draw, candidate, fnt)[0] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def draw_centered_text(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    fnt: ImageFont.FreeTypeFont,
    fill: str,
    line_gap: int = 12,
) -> None:
    heights = [text_size(draw, line, fnt)[1] for line in lines]
    total_h = sum(heights) + line_gap * (len(lines) - 1)
    x1, y1, x2, y2 = box
    y = y1 + (y2 - y1 - total_h) / 2
    for line, h in zip(lines, heights):
        w, _ = text_size(draw, line, fnt)
        draw.text((x1 + (x2 - x1 - w) / 2, y), line, font=fnt, fill=fill)
        y += h + line_gap


def rounded_box(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str, width: int = 4, radius: int = 28) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], fill: str, width: int = 4) -> None:
    draw.line([start, end], fill=fill, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    length = 20
    spread = math.radians(28)
    p1 = (
        end[0] - length * math.cos(angle - spread),
        end[1] - length * math.sin(angle - spread),
    )
    p2 = (
        end[0] - length * math.cos(angle + spread),
        end[1] - length * math.sin(angle + spread),
    )
    draw.polygon([end, p1, p2], fill=fill)


def draw_card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    example: str,
    accent: str,
) -> None:
    x1, y1, x2, y2 = box
    rounded_box(draw, box, fill="#F7FAFE", outline="#C8D7E8", width=3, radius=24)
    draw.rounded_rectangle((x1, y1, x1 + 16, y2), radius=8, fill=accent)
    title_font = font(33, bold=True)
    body_font = font(25)
    small_font = font(22)
    draw.text((x1 + 36, y1 + 28), title, font=title_font, fill=accent)
    body_lines = wrap_text(draw, body, body_font, x2 - x1 - 72)
    y = y1 + 78
    for line in body_lines[:2]:
        draw.text((x1 + 36, y), line, font=body_font, fill="#173A63")
        y += 34
    draw.text((x1 + 36, y2 - 40), example, font=small_font, fill="#607184")


def main() -> int:
    img = Image.new("RGB", (1600, 900), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    deep_blue = "#173A63"
    orange = "#F27A1A"
    green = "#2F7D3A"
    slate = "#6B7B8C"

    draw.text((72, 54), "图1-1 软件复杂性的四个来源", font=font(46, bold=True), fill=deep_blue)
    draw.text((72, 120), "真实系统的复杂性通常来自多类因素叠加，而不是某一段代码本身。", font=font(27), fill=slate)

    center = (580, 334, 1020, 522)
    cards = {
        "tl": (90, 210, 520, 386),
        "tr": (1080, 210, 1510, 386),
        "bl": (90, 540, 520, 716),
        "br": (1080, 540, 1510, 716),
    }

    # Connectors are intentionally short and edge-to-edge. They do not cross node text.
    arrow(draw, (520, 300), (580, 386), fill=deep_blue, width=4)
    arrow(draw, (1080, 300), (1020, 386), fill=deep_blue, width=4)
    arrow(draw, (520, 626), (580, 470), fill=orange, width=4)
    arrow(draw, (1080, 626), (1020, 470), fill=orange, width=4)

    rounded_box(draw, center, fill="#EAF2FB", outline=deep_blue, width=5, radius=34)
    draw_centered_text(draw, center, ["系统", "复杂性"], font(50, bold=True), deep_blue, line_gap=14)

    draw_card(draw, cards["tl"], "需求规模与变化速度", "需求从一个表单扩展为一组业务流程", "例：预约、借用、门禁、统计", deep_blue)
    draw_card(draw, cards["tr"], "团队协作规模", "多人开发时接口、评审、发布都需要协调", "例：前端、后端、测试、运维", deep_blue)
    draw_card(draw, cards["bl"], "技术组合深度", "不同技术和外部服务会带来依赖风险", "例：数据库、缓存、消息、认证", orange)
    draw_card(draw, cards["br"], "运行与交付约束", "并发、故障、权限和回滚会放大问题", "例：超时、越权、日志、备份", orange)

    conclusion = (195, 776, 1405, 840)
    rounded_box(draw, conclusion, fill="#FFF7EF", outline="#F3C49D", width=2, radius=24)
    draw_centered_text(
        draw,
        conclusion,
        ["复杂性不是单点问题，而是需求、协作、技术和运行约束共同作用的结果。"],
        font(27, bold=True),
        "#B95609",
    )

    for target in TARGETS:
        target.parent.mkdir(parents=True, exist_ok=True)
        img.save(target, "PNG", optimize=True)

    # Keep the v5.1 figure cache aligned if it exists.
    v51 = ROOT / "textbook" / "figures_v5_1" / "chapter01" / "student" / OUT_NAME
    if v51.parent.exists():
        shutil.copy2(TARGETS[0], v51)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
