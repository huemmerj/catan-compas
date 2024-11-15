from fastapi import APIRouter

from api.logic.game_logic import solve_optimal_position
from api.models.solver import SolverResponse, SolverPayload

router = APIRouter()


@router.post("/")
async def get_optimal_position(payload: SolverPayload) -> SolverResponse:
    success, solution = solve_optimal_position(payload.problem)
    if success:
        return SolverResponse(status="success", solution=solution)
    else:
        return SolverResponse(status="error", message="No solution found")
