## Student Learning & Grade Prediction
#### J.D. Kilgallin & Heather Michaud


## Questions
 * What are the most difficult problem areas for new CS students?
 * How does the difficulty decrease over time? 
    * How long does it take students to realize and learn from their mistakes?
 * Are certain categories correlated?
    * For example, "Those who didn't understand X, also misunderstood Y"
 * Can previous mistakes be a predictor for future mistakes in lab?


## Data Collection

 * Thus far, data has been collected for section 030 of CS 1 lab
  * 9 assignments
  * 38 students
  * 342 labs 
 * Each assignment has a set of attributes


## Categories

 * code formatting
  * indentation
  * line wrap
  * source comments
  * name/email in header
 * commits
  * descriptive commit messages
  * regular intervals
 * correct output
 * input handled correctly
 * calculations are correct
 * compiles successfully
 * incomplete


## Parsing

 * Data for each lab is contained in an excel sheet by class
 * Convert CSV files containing list of labs and categories to ARFF
   * student, lab, name, commit intervals, commit messages, compiles, output, input, variables, calculation, code formatting
   * amg38,1,yes,yes,yes,no,yes,yes,yes,yes,no
   * amg38,2,yes,yes,yes,yes,yes,yes,yes,yes,no
   * rlh12,1,yes,no,no,yes,yes,yes,yes,yes,yes
   * rlh12,2,yes,yes,no,yes,yes,yes,yes,yes,yes


The goal here is that the prediction will take into account the student's past performance, as well
as how other students did on the lab. 


## Examples

 * "those who missed points for X, also missed points
for Y..."
 * Source comments vs. commit messages


## Results

 * Run training and testing data through WEKA
 * Analyze confusion matrix for power of predictability
 * See how categories trend
    * over time (by lab)
    * by student
 * How categories are related

