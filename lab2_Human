#define _USE_MATH_DEFINES
 
#include <iostream>
#include <cstdint>
#include <cstdlib>
#include <vector>
#include <random>
#include <cmath>

using namespace std;

class Position {
	private:
		double lon;
		double lat;
	public:
		Position(double lon, double lat) {
			this->lon = lon;
			this->lat = lat;
		}
		double get_lon() {
			return this->lon;
		}
		double get_lat() {
			return this->lat;
		}
		void set_lon(double lon) {
			this->lon = lon;
		}
		void set_lat(double lat) {
			this->lat = lat;
		}
		double distance(Position* pos) {
				double lat1 = this->get_lat() / 180.0 * 3.1416926;
				double lon1 = this->get_lon() / 180.0 * 3.1416926;
				double lat2 = pos->get_lat() / 180.0 * 3.1416926;
				double lon2 = pos->get_lon() / 180.0 * 3.1416926;
 
				double lon_r = lon1 - lon2;
				double lat_r = lat1 - lat2;
 
				double a = pow(sin(lat_r / 2.0), 2) + pow(sin(lon_r / 2.0), 2) * cos(lat1) * cos(lat2);
				double c = 2.0 * asin(sqrt(a));
				return 6378137.0 * c;
		}
};
 
class Human {
	private:
		string first_name;
		string last_name;
		double velocity;
		double dir;
		vector<Position> path = vector<Position>();
	public:
		Human(string first_name, string last_name, Position pos) {
			this->set_first_name(first_name);
			this->set_last_name(last_name);
			this->set_velocity(0.0);
			this->set_dir(0.0);
			this->set_position(pos);
		}
		string* get_first_name()  {
			return &this->first_name;
		}
		string* get_last_name() {
			return &this->last_name;
		}
		Position* get_position() {
			return &this->path.back();
		}
		double get_velocity() {
			return this->velocity;
		}
		double get_dir() {
			return this->dir;
		}
		void set_first_name(string first_name) {
			this->first_name = first_name;
		}
		void set_last_name(string last_name) {
			this->last_name = last_name;
		}
		void set_position(Position pos) {
			this->path.push_back(pos);
		}
		void set_velocity(double velocity) {
			this->velocity = velocity;
		}
		void set_dir(double dir) {
			this->dir = dir;
		}
		double distance() {
			double d = 0.0;
 
			for(int i = 0; i < path.size() - 1; i++) {
				d += path[i].distance(&path[i+1]);
			}
			
			return d;
		}
};
 
int main() {
	vector<Human> humans = vector<Human>();

	humans.push_back(Human("Папич", "Винницианский", Position(0, 0)));
	humans.push_back(Human("Мафиозник", "Шумиловский", Position(0, 0)));
	
	for(int i = 0; i < 20; i++) {
		for(int j = 0; j < humans.size(); j++) {
			Human* human = &humans[j];
			human->set_velocity(human->get_velocity() + ((rand() % 200 - 100) / 500.0));
			if(human->get_velocity() > 0.8) {
				human->set_velocity(0.8);
			}
			human->set_dir(human->get_dir() + ((rand() % 200 - 100) / 500.0));
			double lon = human->get_position()->get_lon() + human->get_velocity() * cos(human->get_dir());
			double lat = human->get_position()->get_lat() + human->get_velocity() * sin(human->get_dir());
			human->set_position(Position(lon, lat));
		}
	}

	for(int j = 0; j != humans.size(); j++) {
		Human* human = &humans[j];
		cout << *human->get_first_name() << " " << *human->get_last_name() << " walked the length of " << human->distance() << ".\n";
	}
  
	return 0;
}
