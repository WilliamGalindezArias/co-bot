## 0_consultation
* greet
  - utter_greet
* open_question
  - utter_response_open_question
  
## 1_consultation
* open_question OR what_is_covid OR what_symptoms OR how_spread OR how_spread_air OR tf_transmitted_person_no_sy OR tf_transmitted_person_feces
  - action_question

## 2_consultation
* what_todo_protect OR should_worry OR how_risky OR do_antibi_help OR do_medici_exist OR is_there_vaccine OR should_use_mask OR how_long_incubation
  - action_question

## 3_consultation
* does_my_pet_get_infected OR can_open_packages OR want_know_more OR do_medici_exist OR is_there_vaccine OR should_use_mask
  - action_question

## 4_consultation
* greet
  - utter_greet
* does_my_pet_get_infected OR can_open_packages OR want_know_more OR do_medici_exist OR is_there_vaccine OR should_use_mask
  - action_question
  
## 5_consultation
* greet
  - utter_greet
* open_question OR what_is_covid OR what_symptoms OR how_spread OR how_spread_air OR tf_transmitted_person_no_sy OR tf_transmitted_person_feces
  - action_question