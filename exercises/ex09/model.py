"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730566282"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Finds distance between two points."""
        result: float = sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))
        return result


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Updates cell."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Sets colors of cells."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "red"
        if self.is_immune():
            return "green"

    def contract_disease(self) -> None:
        """Assigns INFECTED to sickness."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Tells if cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Tells if cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, other: Cell):
        """Method called when two Cell objects make contact."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        elif self.is_vulnerable() and other.is_infected():
            self.contract_disease()

    def immunize(self) -> None:
        """Assigns IMMUNE to sickness."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> None:
        """Tells if cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
        

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, numinfected: int, numimmune: int = 0):
        """Initialize the cells with random locations and directions."""
        if (numinfected + numimmune) == cells or (numinfected + numimmune) <= 0:
            raise ValueError("Too many infected and immune")
        if numinfected == cells or numinfected <= 0:
            raise ValueError("Correct number of infected")
        self.population = []
        for i in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for i in range(numinfected):
            self.population[i + 1].sickness = constants.INFECTED
        for i in range(numimmune):
            self.population[i].sickness = constants.IMMUNE
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x < constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y < constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        recovered: list[bool] = []
        for cells in self.population:
            if cells.immunize() or cells.is_vulnerable():
                recovered.append(cells.immunize() or cells.is_vulnerable())
        if len(recovered) < constants.CELL_COUNT:
            return False
        else:
            return True

    def check_contacts(self) -> None:
        """Checks if cells are touching."""
        i: int = 0
        for i in range(len(self.population)):
            for j in range(len(self.population)):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])