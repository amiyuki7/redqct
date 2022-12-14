from __future__ import annotations
from typing import Optional, List
from discord import Status, Colour
import json

with open("namemap.json", "r") as f:
    """
    NAMEMAP is in this structure:
    {
        "game_name": {
            "application_id": str
            "icon_hash": Optional[str]
        },
        ...
    }
    """
    NAMEMAP: dict[str, dict[str, Optional[str]]] = json.load(f)


class MemberAttrs:
    def __init__(
        self,
        name: str,
        tag: str,
        nick: Optional[str],
        status: Status,
        avatar: str,
        banner_colour: Optional[Colour],
        # badges: List[discord.PublicUserFlags] | None,
        activities: List[ActivityAttrs],
        customActivity: Optional[str],
    ) -> None:
        self.name = name
        self.tag = tag
        self.nick = nick
        self.status = status
        self.avatar = avatar
        self.banner_colour = banner_colour
        # self.badges = badges
        self.activities = activities
        self.customActivity = customActivity


class ActivityAttrs:
    def __init__(
        self,
        activity_type: str,
        image_large: str,
        image_small: str,
        line1: str,
        line2: str,
        line3: str,
        line4: str,
    ) -> None:
        self.type = activity_type
        self.image_large = image_large
        self.image_small = image_small
        # self.line1 = len(line1) > 35 and line1[:50] + "..." or line1
        # self.line2 = len(line2) > 35 and line2[:50] + "..." or line2
        # self.line3 = len(line3) > 35 and line3[:50] + "..." or line3
        # self.line4 = len(line4) > 35 and line4[:50] + "..." or line4
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4


Number = int | float


def cube(x: Number) -> Number:
    """
    Returns the cube of a number up to 3 decimal places
    """
    return round(x**3, 3)
