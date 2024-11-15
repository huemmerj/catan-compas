from typing import Literal, Optional, Union
from pydantic import BaseModel, Field


class SolverPayload(BaseModel):
    problem: dict[str, tuple[int, str]] = Field(
        ...,
        title="Problem to solve",
        description="The problem to solve",
        examples=[
            {
                "hex1": [7, "desert"],
                "hex2": [8, "wood"],
                "hex3": [9, "sheep"],
                "hex4": [12, "brick"],
                "hex5": [5, "wheat"],
                "hex6": [10, "sheep"],
                "hex7": [10, "wood"],
                "hex8": [9, "sheep"],
                "hex9": [4, "wood"],
                "hex10": [6, "brick"],
                "hex11": [3, "ore"],
                "hex12": [6, "wheat"],
                "hex13": [5, "ore"],
                "hex14": [2, "wheat"],
                "hex15": [4, "wood"],
                "hex16": [11, "ore"],
                "hex17": [11, "wheat"],
                "hex18": [3, "brick"],
                "hex19": [8, "sheep"],
            },
        ],
    )


class SolverResponse(BaseModel):
    status: Union[Literal["success"], Literal["error"]]
    message: Optional[str] = None
    solution: Optional[list] = None
