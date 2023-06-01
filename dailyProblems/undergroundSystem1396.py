class UndergroundSystem:


	def __init__(self):
		self.passengers = {} # each passenger id -> {inStation,inTime,outStation,outTime}
		self.stations = {}
		pass

	def checkIn(self, id: int,stationName: str,t: int) -> None:
		self.passengers[id] = {
			"inStation": stationName,
			"inTime": t
		}

	def checkOut(self, id: int,stationName: str,t: int) -> None:
		self.passengers[id]["outStation"] = stationName
		self.passengers[id]["outTime"] = t
		if (self.passengers[id]['inStation'],self.passengers[id]['outStation']) not in self.stations:
			self.stations[(self.passengers[id]['inStation'],self.passengers[id]['outStation'])] = []
		self.stations[(self.passengers[id]['inStation'],self.passengers[id]['outStation'])].append(self.passengers[id]['outTime'] - self.passengers[id]['inTime'])

	def getAverageTime(self,startStation: str,endStation: str) -> float:
		return sum(self.stations[(startStation,endStation)]) / len(self.stations[(startStation,endStation)])


undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(101,"tpt",0)
undergroundSystem.checkIn(102,"bgl",0)
undergroundSystem.checkOut(101,"bgl",10)
undergroundSystem.checkOut(102,"tpt",8)
undergroundSystem.checkIn(103,"tpt",4)
undergroundSystem.checkOut(103,"bgl",21)
print(undergroundSystem.getAverageTime("tpt","bgl"))