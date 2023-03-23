<?php
$images = $_POST['images'];
$quantity = $_POST['quantity'];

// Create new PDF document
$pdf = new \FPDF();

// Loop through selected images and add to PDF
foreach ($images as $image) {
  $pdf->AddPage();
  $pdf->Image($image, 10, 10, 100);
}

// Save PDF to file
$pdf->Output('images.pdf', 'D');
?>
