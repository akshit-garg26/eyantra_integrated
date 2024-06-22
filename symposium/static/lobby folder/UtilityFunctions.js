  //This function calculates the offsetted position based on the base_positions of current_room and using an offset times room index
  function GenerateCalculatedPositions(room_index, current_room, base_positions) {
    let offset = 10;

    // Initialize arrays for storing calculated positions
    let calculated_positions = []; // Stores the calculated positions for each room
    let current_position = []; // Stores the current position being calculated
    let base_position_of_current_room = base_positions[current_room]; // Get the base position of the current room from the base_positions array

    // Loop to calculate positions for each room
    for (let i = 0; i < 4; i++) {
      current_position = []; // Reset the current position array for each iteration

      // Loop to calculate the X, Y, and Z coordinates of the current position
      for (let j = 0; j < 3; j++) {
        current_position.push(
          j === 0
            ? base_position_of_current_room[i][j] + (offset * room_index) // Calculate the X coordinate with an additional offset based on the room index
            : base_position_of_current_room[i][j] // Use the base position for the Y and Z coordinates
        );
      }

      calculated_positions.push(current_position); // Add the calculated position to the array of calculated positions
    }

    //console.log(calculated_positions, calculated_light_positions);
    return [calculated_positions];
  }
