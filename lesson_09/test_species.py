import pytest

from db import execute_query


@pytest.fixture
def test_species():
    result = execute_query(
        """
        SELECT COALESCE(MAX(species_id), 0) + 1 AS species_id
        FROM species
        """
    )

    species_id = result.fetchone().species_id

    execute_query(
        """
        INSERT INTO species (
            species_id,
            type_id,
            species_name,
            species_amount,
            date_start,
            species_status
        )
        VALUES (
            :species_id,
            :type_id,
            :species_name,
            :species_amount,
            :date_start,
            :species_status
        )
        """,
        {
            "species_id": species_id,
            "type_id": 2,
            "species_name": "тестовое животное",
            "species_amount": 1,
            "date_start": "2026-08-30",
            "species_status": "active"
        }
    )

    yield species_id

    execute_query(
        """
        DELETE FROM species
        WHERE species_id = :species_id
        """,
        {"species_id": species_id}
    )


def test_add_species(test_species):
    result = execute_query(
        """
        SELECT species_name
        FROM species
        WHERE species_id = :species_id
        """,
        {"species_id": test_species}
    )

    species = result.fetchone()

    assert species.species_name == "тестовое животное"


def test_update_species(test_species):
    execute_query(
        """
        UPDATE species
        SET species_name = :species_name
        WHERE species_id = :species_id
        """,
        {
            "species_id": test_species,
            "species_name": "измененное животное"
        }
    )

    result = execute_query(
        """
        SELECT species_name
        FROM species
        WHERE species_id = :species_id
        """,
        {"species_id": test_species}
    )

    species = result.fetchone()

    assert species.species_name == "измененное животное"


def test_delete_species():
    result = execute_query(
        """
        SELECT COALESCE(MAX(species_id), 0) + 1 AS species_id
        FROM species
        """
    )

    species_id = result.fetchone().species_id

    execute_query(
        """
        INSERT INTO species (
            species_id,
            type_id,
            species_name,
            species_amount,
            date_start,
            species_status
        )
        VALUES (
            :species_id,
            :type_id,
            :species_name,
            :species_amount,
            :date_start,
            :species_status
        )
        """,
        {
            "species_id": species_id,
            "type_id": 2,
            "species_name": "животное для удаления",
            "species_amount": 1,
            "date_start": "2026-08-30",
            "species_status": "active"
        }
    )

    execute_query(
        """
        DELETE FROM species
        WHERE species_id = :species_id
        """,
        {"species_id": species_id}
    )

    result = execute_query(
        """
        SELECT species_id
        FROM species
        WHERE species_id = :species_id
        """,
        {"species_id": species_id}
    )

    assert result.fetchone() is None
