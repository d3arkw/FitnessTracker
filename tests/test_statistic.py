from app.services.statistics_service import get_statistics
import pytest


@pytest.mark.asyncio
async def test_get_statistics(db_session,test_user,seed_fitness):
    result = await get_statistics(db=db_session,current_user=test_user)
    assert result is not None
    assert result.total_workouts == 1
    assert result.total_exercises == 2
    assert result.best_bench_press == 160
    assert result.total_volume == 1260