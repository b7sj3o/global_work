function createPreview(input, previewContainerId, fileType) {
    const previewContainer = document.getElementById(previewContainerId);
    previewContainer.innerHTML = "";

    const dt = new DataTransfer();

    Array.from(input.files).forEach((file) => {
        dt.items.add(file);
    });


    // show selected images || videos
    Array.from(dt.files).forEach((file, index) => {
        const reader = new FileReader();
        const previewItem = document.createElement("div");
        previewItem.className = fileType === "image" ? "preview-item" : "preview-item-video";

        reader.onload = (e) => {
            if (fileType === "image") {
                previewItem.innerHTML = `
                    <img src="${e.target.result}" alt="Image Preview" class="preview-image" />
                    <button type="button" class="preview-remove" data-index="${index}">&times;</button>
                `;
            } else if (fileType === "video") {
                previewItem.innerHTML = `
                    <video controls class="preview-video">
                        <source src="${e.target.result}" type="${file.type}">
                        Your browser does not support the video tag.
                    </video>
                    <button type="button" class="preview-remove" data-index="${index}">&times;</button>
                `;
            }
            previewContainer.appendChild(previewItem);
        };

        reader.readAsDataURL(file);
    });

    // remove previews
    previewContainer.onclick = function (e) {
        if (e.target.classList.contains("preview-remove")) {
            const indexToRemove = parseInt(e.target.dataset.index);

            const newDt = new DataTransfer();
            Array.from(dt.files).forEach((file, index) => {
                if (index !== indexToRemove) {
                    newDt.items.add(file);
                }
            });

            input.files = newDt.files;
            createPreview(input, previewContainerId, fileType);
        }
    };
}

document.getElementById("mainImageInput").addEventListener("change", function () {
    createPreview(this, "mainImagePreview", "image");
});

document.getElementById("additionalImagesInput").addEventListener("change", function () {
    createPreview(this, "additionalImagesPreview", "image");
});

document.getElementById("videoInput").addEventListener("change", function () {
    createPreview(this, "videoPreview", "video");
});
