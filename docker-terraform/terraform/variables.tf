variable "credentials" {
  description = "My Credentials"
  default     = "./keys/my-cred.json"
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}

variable "project" {
  description = "Project Id"
  default     = "single-odyssey-450310-d6"
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}

variable "bq_dataset_name" {
  description = "My BigQuery Name"
  default     = "demo_dataset"
}

variable "location" {
  description = "My Project Location"
  default     = "US"
}

variable "gcs_bucket_name" {
  description = "Storage Bucket Name"
  default     = "single-odyssey-450310-d6-terraform-demo-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDART"
}