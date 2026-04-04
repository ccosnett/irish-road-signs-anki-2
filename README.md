# Irish Road Signs

A collection of Irish road signs for studying for the Irish driving test.

Each image filename is a description of the sign.

## Anki Deck

This repository can generate an Anki deck where the front of each card is the sign image and the back is the sign description derived from the filename.

### Load the Deck in Anki

1. Install Anki from [apps.ankiweb.net](https://apps.ankiweb.net/) if you do not already have it.
2. Open Anki on your computer.
3. In Anki, click `File` -> `Import`.
4. Select `dist/irish-road-signs.apkg` from this repository.
5. Confirm the import when Anki shows the deck preview.
6. Open the imported `Irish Road Signs` deck.
7. Start studying. Each card shows the sign image first, and the answer reveals the sign description.

If you want the latest version of the deck package before importing, rebuild it first:

Build the deck with:

```bash
python3 scripts/build_anki_deck.py
```

The generated package is written to `dist/irish-road-signs.apkg`.

### Automatic Deck Updates

This repository now updates the generated Anki deck automatically.

- The GitHub Actions workflow at `.github/workflows/update-anki-deck.yml` rebuilds `dist/irish-road-signs.apkg` when sign images or the deck script change on `main`.
- Pull requests that change sign images or the deck script also verify that the checked-in `.apkg` file is up to date.
- The deck build is deterministic, so rebuilding the same inputs should produce the same `.apkg` binary.

### Supported Image Files

The deck builder currently includes tracked image files in the repository root with these extensions:

- `.png`
- `.svg`
- `.jpg`
- `.jpeg`

### Adding a New Sign

1. Add the image file to the repository root.
2. Name the file with the sign description, using underscores between words, for example `mini_roundabout_ahead.svg`.
3. Commit and push the image to `main`, or merge a pull request containing it.
4. The workflow should rebuild `dist/irish-road-signs.apkg` automatically.
5. If needed, you can still rebuild locally with `python3 scripts/build_anki_deck.py`.

## Regulatory Signs

| | | | |
|---|---|---|---|
| ![No Entry](no_entry.png) | ![Per Axle Restriction](per_axle_restriction.png) | ![Clearway](clearway.png) | ![No Straight Ahead](no_straight_ahead.png) |
| ![No Right Turn](no_right_turn.png) | ![No Left Turn](no_left_turn.png) | ![No Overtaking](no_overtaking.png) | ![No Entry for HGV Over 3t](no_entry_for_hgv_over_3t.png) |
| ![Rural Speed Limit 60 km per hour](rural_speed_limit_60_km_per_hour.png) | ![Rural Speed Limit 80 km per hour](rural_speed_limit_80_km_per_hour.png) | ![Speed Limit 50 km per hour](speed_limit_50_km_per_hour.png) | ![Height Restriction](height_restriction.png) |
| ![No U-Turn](no_u_turn.png) | ![Parking Permitted](parking_permitted.png) | ![Parking Prohibited](parking_prohibited.png) | ![Taxi Rank](taxi_rank.png) |
| ![Pedestrian Zone](pedestrian_zone.png) | ![HGV Weight Restriction](hgv_weight_restriction.png) | ![HGV Length Restriction](hgv_length_restriction.png) | ![HGV Width Restriction](hgv_width_restriction.png) |
| ![Right Lane for HGV with Over 3 Axles](right_lane_for_hgv_with_over_3_axles.png) | ![No Horse Riding](no_horse_riding.png) | ![No Pedal Cycles](no_pedal_cycles.png) | ![Cul De Sac Dead End](cul_de_sac_dead_end.png) |

## Information Signs

| | | | |
|---|---|---|---|
| ![Motorway Ahead](motorway_ahead.png) | ![Motorway Ahead Slip Road](motorway_ahead_slip_road.png) | ![300m Until Next Exit](300m_until_next_exit.png) | ![End of Motorway in 500m](end_of_motorway_in_500m.png) |
| ![End of Motorway](end_of_motorway.png) | ![Shared Track](shared_track.png) | ![Cycle Track on Left](cycle_track_on_left.png) | ![Hospital in 100m](hospital_in_100m.png) |

## Roadworks Warning Signs

| | | | |
|---|---|---|---|
| ![Roadworks Ahead](roadworks_ahead.png) | ![End Roadwork](end_roadwork.png) | ![Two Way Traffic](two_way_traffic.png) | ![One Lane Crossover Right](one_lane_crossover_right.png) |
| ![One Lane Crossover Left](one_lane_crossover_left.png) | ![Start Central Obstruction](start_central_obstruction.png) | ![End Central Obstruction](end_central_obstruction.png) | ![Merge to the Right](merge_to_the_right.png) |
| ![Road Narrows Left](road_narrows_left.png) | ![Road Narrows Right](road_narrows_right.png) | ![Road Narrows Left and Right](road_narrows_left_and_right.png) | ![Merging from Left](merging_from_left.png) |
| ![Uneven Surface](uneven_surface.png) | ![Loose Chippings](loose_chippings.png) | ![Nearside Lane Closed](nearside_lane_closed.png) | ![Flagman Ahead](flagman_ahead.png) |
| ![Temporary Traffic Signals](temporary_traffic_signals.png) | ![Offside Lanes Closed](offside_lanes_closed.png) | ![Move to Right 2 Lanes](move_to_right_2_lanes.png) | ![Move to Left 2 Lanes](move_to_left_2_lanes.png) |
| ![Move to Right 1 Lane](move_to_right_1_lane.png) | ![Single Lane](single_lane.png) | ![Site Access on Left](site_access_on_left.png) | ![Pedestrians Cross to Left](pedestrians_cross_to_left.png) |
| ![Lanes Diverge](lanes_diverge.png) | ![Lanes Crossover Out](lanes_crossover_out.png) | ![Lanes Rejoin Crossover](lanes_rejoin_crossover.png) | ![Lanes Crossover Back](lanes_crossover_back.png) |
| ![Site Access](site_access.png) | ![Site Access on Right](site_access_on_right.png) | ![Queues Likely](queues_likely.png) | ![Pedestrians Cross to Right](pedestrians_cross_to_right.png) |

## Road Markings

| | | | |
|---|---|---|---|
| ![All Traffic Must Keep to the Left of the Line](all_traffic_must_keep_to_the_left_of_the_line.png) | ![You Must Not Cross Unless Safe to Do So](you_must_not_cross_unless_safe_to_do_so.png) | ![Approach of a Hill Crest Bend or Continuous Line](approach_of_a_hill_crest_bend_or_continuous_line.png) | ![No Parking During Shown Times](no_parking_during_shown_times.png) |
| ![Junction Box](junction_box.png) | ![Continuous White Line Shortly Ahead](continuous_white_line_shortly_ahead.png) | ![Must Obey the Line That Is Nearest to Us](must_obey_the_line_that_is_nearest_to_us.png) | ![No Entry Road Markings](no_entry_road_markings.png) |
| ![No Parking at Any Time](no_parking_at_any_time.png) | ![Zebra Pedestrian Crossing](zebra_pedestrian_crossing.png) | | |
