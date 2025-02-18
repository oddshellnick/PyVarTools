import math
import numpy
from typing import (
	Any,
	Generator,
	Literal,
	Optional,
	Union
)


class GraphPoint:
	"""
	Represents a point on a graph with x and y coordinates.

	Attributes:
		x (Union[int, float]): The x-coordinate of the point.
		y (Union[int, float]): The y-coordinate of the point.

	:Usage:
		point = GraphPoint(1, 2)
		(1, 2)

		point = GraphPoint(1.5, 2.5)
		(1.5000, 2.5000)
	"""
	
	def __init__(self, x: Union[int, float], y: Union[int, float]):
		"""
		Initializes a new GraphPoint.

		Args:
			x (Union[int, float]): The x-coordinate.
			y (Union[int, float]): The y-coordinate.
		"""
		self.x = x
		self.y = y
	
	def __str__(self) -> str:
		"""
		Returns a string representation of the point.

		Returns:
			str: String representation of the point.
		"""
		x_string = f"{self.x:.4f}" if isinstance(self.x, float) else str(self.x)
		y_string = f"{self.y:.4f}" if isinstance(self.y, float) else str(self.y)
		
		return f"({x_string}, {y_string})"
	
	def __repr__(self) -> str:
		"""
		Returns a string representation of the point.

		Returns:
			str: String representation of the point.
		"""
		return str(self)


def calculate_angle_degree(start_point: GraphPoint, end_point: GraphPoint) -> float:
	"""
	Calculates the angle in degrees between two GraphPoints.

	Args:
		start_point (GraphPoint): The starting point.
		end_point (GraphPoint): The ending point.

	Returns:
		float: The angle in degrees.

	:Usage:
		p1 = GraphPoint(1, 1)
		p2 = GraphPoint(2, 2)
		calculate_angle_degree(p1, p2)
		45.0
	"""
	if start_point.y == end_point.y:
		return 0.0
	else:
		if end_point.x == start_point.x:
			return 90
	
		tanh = (end_point.y - start_point.y) / (end_point.x - start_point.x)
		return math.degrees(math.atan(tanh))


class GraphSection:
	"""
	Represents a section of a graph defined by a list of GraphPoints.

	Attributes:
		points (list[GraphPoint]): The list of points in the section.
		angle_sensitivity (float): The sensitivity for determining the direction of the section.
		min (GraphPoint): The point with the minimum y-value.
		max (GraphPoint): The point with the maximum y-value.
		average (float): The average y-value of the points.

	:Usage:
		points = [GraphPoint(1, 1), GraphPoint(2, 2), GraphPoint(3, 3)]
		section = GraphSection(points)
		[(1, 1), (2, 2), (3, 3)] (num_points: 3, min: (1, 1), max: (3, 3), average: 2.0000, direction: increasing)
	"""
	
	def __init__(self, points: list[GraphPoint], angle_sensitivity: float = 0.0):
		"""
		Initializes a new GraphSection.

		Args:
			points (list[GraphPoint]): The list of GraphPoints.
			angle_sensitivity (float): The angle sensitivity. Defaults to 0.0.

		Raises:
			ValueError: If angle_sensitivity is less than 0.0.
		"""
		if angle_sensitivity < 0.0:
			raise ValueError("angle_sensitivity must be >= 0.0")
		
		self.points = points
		self.angle_sensitivity = angle_sensitivity
		
		self.min = min(points, key=lambda point: point.y)
		
		self.max = max(points, key=lambda point: point.y)
		
		self.average = numpy.mean([point.y for point in self.points]).item()
	
	def __str__(self) -> str:
		"""
		Returns a string representation of the section.

		Returns:
			str: String representation of the section.
		"""
		min_string = f"{self.min.y:.4f}" if isinstance(self.min.y, float) else str(self.min.y)
		max_string = f"{self.max.y:.4f}" if isinstance(self.max.y, float) else str(self.max.y)
		average_string = f"{self.average:.4f}" if isinstance(self.average, float) else str(self.average)
		
		return f"{self.points} (num_points: {len(self.points)}, min: ({self.min.x},{min_string}), max: ({self.max.x},{max_string}), average: {average_string}, direction: {self.get_direction()})"
	
	def __repr__(self) -> str:
		"""
		Returns a string representation of the section.

		Returns:
			str: String representation of the section.
		"""
		return str(self)
	
	def calculate_average(self):
		"""Calculates and updates the average y-value."""
		self.average = numpy.mean([point.y for point in self.points]).item()
	
	def add(self, point: GraphPoint):
		"""
		Adds a point to the section and updates min, max, and average.

		Args:
			point (GraphPoint): The point to add.
		"""
		self.points.append(point)
		
		if point.y < self.min.y:
			self.min = point
		
		if point.y > self.max.y:
			self.max = point
		
		self.calculate_average()
	
	def get_angle_degree(self) -> Optional[float]:
		"""
		Calculates the angle of the section.

		Returns:
			Optional[float]: The angle in degrees, or None if the section has less than two points.
		"""
		if len(self.points) >= 2:
			return calculate_angle_degree(self.points[0], self.points[-1])
		else:
			return None
	
	def get_direction(self) -> Optional[str]:
		"""
		Determines the direction of the section.

		Returns:
			Optional[str]: The direction ("increasing", "decreasing", "straight"), or None if the section has less than two points.
		"""
		if len(self.points) >= 2:
			angle = self.get_angle_degree()
			if angle is None:
				return None
		
			if angle > self.angle_sensitivity:
				return "increasing"
			elif angle < -self.angle_sensitivity:
				return "decreasing"
			else:
				return "straight"
		else:
			return None
	
	def get_graph_points_after_max(self) -> list[GraphPoint]:
		"""
		Returns the points after the maximum y-value point.

		Returns:
			list[GraphPoint]: The points after the maximum.
		"""
		return self.points[self.points.index(self.max):]
	
	def get_graph_points_after_min(self) -> list[GraphPoint]:
		"""
		Returns the points after the minimum y-value point.

		Returns:
			list[GraphPoint]: The points after the minimum.
		"""
		return self.points[self.points.index(self.min):]
	
	def remove_point_after_max(self):
		"""
		Removes points in the section after the maximum y-value point and recalculates the average.
		"""
		self.points = self.points[: self.points.index(self.max) + 1]
		self.calculate_average()
	
	def remove_point_after_min(self):
		"""
		Removes points in the section after the minimum y-value point and recalculates the average.
		"""
		self.points = self.points[: self.points.index(self.min) + 1]
		self.calculate_average()


class ThresholdSensitivity:
	"""
	Represents the sensitivity for threshold-based comparisons.

	Attributes:
		threshold_sensitivity (float): The sensitivity value.
		type_ (Literal["absolute", "relative"]): The type of sensitivity ("absolute" or "relative").

	:Usage:
		sensitivity = ThresholdSensitivity(0.1, "relative")
		sensitivity.get_increase_sensitive_point(1)
		1.1
	"""
	
	def __init__(
			self,
			threshold_sensitivity: float = 0.0,
			type_: Literal["absolute", "relative"] = "absolute"
	):
		"""
		Initializes a new ThresholdSensitivity object.

		Args:
			threshold_sensitivity (float): The sensitivity value. Defaults to 0.0.
			type_ (Literal["absolute", "relative"]): The type of sensitivity. Defaults to "absolute".

		Raises:
			ValueError: If type_ is not "absolute" or "relative".
		"""
		if type_ not in ["absolute", "relative"]:
			raise ValueError('type_ must be "absolute" or "relative"')
		
		self.threshold_sensitivity = threshold_sensitivity
		self.type_ = type_
	
	def get_decrease_sensitive_point(self, point: Union[GraphPoint, int, float]) -> float:
		"""
		Calculates the decreased sensitive point based on the sensitivity type.

		Args:
			point (Union[GraphPoint, int, float]): The point or value to adjust.

		Returns:
			float: The decreased sensitive point.
		"""
		decrease_sensitive_point = point.y if isinstance(point, GraphPoint) else point
		
		if self.type_ == "absolute":
			return decrease_sensitive_point - self.threshold_sensitivity
		
		if self.type_ == "relative":
			return decrease_sensitive_point * (1 - self.threshold_sensitivity)
	
	def get_increase_sensitive_point(self, point: Union[GraphPoint, int, float]) -> float:
		"""
		Calculates the increased sensitive point based on the sensitivity type.

		Args:
			point (Union[GraphPoint, int, float]): The point or value to adjust.

		Returns:
			float: The increased sensitive point.
		"""
		increase_sensitive_point = point.y if isinstance(point, GraphPoint) else point
		
		if self.type_ == "absolute":
			return increase_sensitive_point + self.threshold_sensitivity
		
		if self.type_ == "relative":
			return increase_sensitive_point * (1 + self.threshold_sensitivity)


class Graph:
	"""
	Represents a graph composed of GraphPoints.

	Attributes:
		points (list[GraphPoint]): The list of points in the graph.
		min (Optional[GraphPoint]): The point with the minimum y-value.
		max (Optional[GraphPoint]): The point with the maximum y-value.
		average (Optional[float]): The average y-value of all points.

	:Usage:
		graph = Graph([GraphPoint(1, 1), GraphPoint(2, 2)])
		(num_points: 2, min: 1, max: 2, average: 1.5000)
	"""
	
	def __init__(self, points: Optional[list[GraphPoint]] = None):
		"""
		Initializes a new Graph object.

		Args:
			points (Optional[list[GraphPoint]]): Initial list of points. Defaults to None.
		"""
		if points is not None:
			self.points = points
			
			self.min = min(points, key=lambda point: point.y) if points else None
			
			self.max = max(points, key=lambda point: point.y) if points else None
			
			self.average = numpy.mean([point.y for point in self.points]).item() if points else None
		else:
			self.points = []
			self.min = None
			self.max = None
			self.average = None
	
	def __str__(self) -> str:
		"""
		Returns a string representation of the graph.

		Returns:
			str: The string representation.
		"""
		min_string = f"{self.min.y:.4f}" if self.min and isinstance(self.min.y, float) else str(self.min)
		max_string = f"{self.max.y:.4f}" if self.max and isinstance(self.max.y, float) else str(self.max)
		average_string = (
				f"{self.average:.4f}"
				if self.average
				and isinstance(self.average, float)
				else str(self.average)
		)
		
		return f"(num_points: {len(self.points)}, min: {min_string}, max: {max_string}, average: {average_string})"
	
	def __repr__(self) -> str:
		"""
		Returns a string representation of the graph.

		Returns:
			str: The string representation.
		"""
		return self.__str__()
	
	def calculate_average(self):
		"""
		Calculates and updates the average y-value.
		"""
		if self.points:
			self.average = numpy.mean([point.y for point in self.points]).item()
	
	def add(self, point: GraphPoint):
		"""
		Adds a point to the graph and updates min, max, and average.

		Args:
			point (GraphPoint): The point to add.
		"""
		self.points.append(point)
		
		if self.min is None or point.y < self.min.y:
			self.min = point
		
		if self.max is None or point.y > self.max.y:
			self.max = point
		
		self.calculate_average()
	
	def get_sections(
			self,
			threshold_sensitivity: ThresholdSensitivity = ThresholdSensitivity(),
			angle_sensitivity: float = 0.0
	) -> Generator[GraphSection, Any, None]:
		"""
		Divides the graph into sections based on threshold and angle sensitivity.

		Args:
			threshold_sensitivity (ThresholdSensitivity, optional): The threshold sensitivity. Defaults to ThresholdSensitivity().
			angle_sensitivity (float, optional): The angle sensitivity. Defaults to 0.0.

		Returns:
		   Generator[GraphSection, Any, None]: A generator of GraphSections.
		"""
		graph_section = None
		
		for i in range(len(self.points)):
			if graph_section is None:
				graph_section = GraphSection([self.points[i]], angle_sensitivity)
			else:
				direction = graph_section.get_direction()
		
				if direction is None:
					graph_section.add(self.points[i])
				elif direction == "increasing":
					if self.points[i].y > threshold_sensitivity.get_decrease_sensitive_point(graph_section.max):
						graph_section.add(self.points[i])
					else:
						start_of_new_section = graph_section.get_graph_points_after_max()
						graph_section.remove_point_after_max()
		
						yield graph_section
		
						graph_section = GraphSection(start_of_new_section + [self.points[i]], angle_sensitivity)
				elif direction == "decreasing":
					if self.points[i].y < threshold_sensitivity.get_increase_sensitive_point(graph_section.min):
						graph_section.add(self.points[i])
					else:
						start_of_new_section = graph_section.get_graph_points_after_min()
						graph_section.remove_point_after_min()
		
						yield graph_section
		
						graph_section = GraphSection(start_of_new_section + [self.points[i]], angle_sensitivity)
				elif direction == "straight":
					if (
							self.points[i].y < threshold_sensitivity.get_increase_sensitive_point(graph_section.average)
							or self.points[i].y > threshold_sensitivity.get_decrease_sensitive_point(graph_section.average)
					):
						graph_section.add(self.points[i])
					else:
						yield graph_section
						graph_section = GraphSection([self.points[i]], angle_sensitivity)
		
		if graph_section is not None:
			yield graph_section
