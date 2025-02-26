<?php
if (isset($_GET['file'])) {
    $file = $_GET['file'];

    // Normalize path (Prevent ../../ traversal)
    $filepath = realpath($file);
    $baseDir = realpath(__DIR__); // Ensure file is inside web directory

    if (strpos($filepath, $baseDir) === 0 && file_exists($filepath)) {
        // If it's a text file, allow download
        if (pathinfo($filepath, PATHINFO_EXTENSION) == "txt") {
            header('Content-Type: application/octet-stream');
            header('Content-Disposition: attachment; filename="' . basename($filepath) . '"');
            readfile($filepath);
            exit;
        }

        // Otherwise, just display the file
        echo "<pre>" . htmlspecialchars(file_get_contents($filepath)) . "</pre>";
    } else {
        echo "Invalid file.";
    }
} else {
    echo "No file specified.";
}
?>


