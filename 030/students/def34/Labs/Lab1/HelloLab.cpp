/********************************************************************
 * $Id$                                                             *
 *                                                                  *
 * Lab 1 : HelloLab.cpp                                             *
 *                                                                  *
 * Author: David E. Fay                                             *
 *         def34@zips.uakron.edu                                    *
 *                                                                  *
 * Purpose: Demonstration of a simple program                       *
 *                                                                  *
 ********************************************************************/

#include <iostream>

using namespace std;

int main() {
   // Prints welcome message...
  // variables for payrate and hours
  int payrate = 7;
  int hours = 40;
     int totalPay = payrate * hours;
      cout << "Total pay: $" << totalPay << ".00" << endl;
}
