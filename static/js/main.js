function addBlock() {
    // Add a new block to the prompt form.
    // You might need to adjust this to match your form structure and server-side logic.
    const blocksContainer = document.getElementById("blocks-container");
    const block = document.createElement("div");
    block.classList.add("prompt-block");
    block.innerHTML = `
      <label>Block Type</label>
      <select class="form-control">
        <option value="instruction">Instruction</option>
        <option value="task_text">Task Text</option>
        <option value="additional_comments">Additional Comments</option>
        <option value="code">Code</option>
      </select>
      <label>Content</label>
      <textarea class="form-control"></textarea>
      <button type="button" class="btn btn-danger" onclick="removeBlock(this)">Remove Block</button>
    `;
    blocksContainer.appendChild(block);
  }
  
  function removeBlock(blockElement) {
    // Remove a block from the prompt form.
    blockElement.parentElement.remove();
  }
  
  //not tested
  function updateBlockOrder() {
    // Update the order of the blocks in the prompt form based on user input.
    // This function will depend on the specific implementation of your form and how you manage block order.
  
      // Get the prompt form and its blocks
      const form = document.querySelector("#prompt-form");
      const blocks = Array.from(form.querySelectorAll(".block"));
    
      // Sort the blocks based on user input
      blocks.sort((a, b) => {
        const aIndex = parseInt(a.querySelector(".block-index").textContent);
        const bIndex = parseInt(b.querySelector(".block-index").textContent);
        return aIndex - bIndex;
      });
    
      // Reorder the blocks in the prompt form
      blocks.forEach((block, index) => {
        block.querySelector(".block-index").textContent = index + 1;
        form.appendChild(block);
      });
    
  
  }
  
  function copyToClipboard(text) {
    // Copy the given text to the clipboard.
    const textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
  }
  
  // Add event listeners for adding blocks and other interactions if necessary.
  document.getElementById("add-block-btn").addEventListener("click", addBlock);

  