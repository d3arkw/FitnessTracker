from app.services.statistics_service import get_statistics,get_best_result
import pytest


@pytest.mark.asyncio
async def test_get_statistics(db_session,test_user,seed_fitness):
    result = await get_statistics(db=db_session,current_user=test_user)
    assert result is not None
    assert result.total_workouts == 1
    assert result.total_exercises == 2
    assert result.best_bench_press == 160
    assert result.total_volume == 1260

@pytest.mark.asyncio
async def test_get_best_result(db_session,test_user,seed_fitness):
    result = await get_best_result(db=db_session,current_user=test_user)
    assert result is not None
    assert len(result) == 2
    assert result[0].max_weight == 160
    assert result[1].max_weight == 200
    assert result[0].exercise == "Bench Press"