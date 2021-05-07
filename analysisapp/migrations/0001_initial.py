# Generated by Django 3.1.2 on 2021-03-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('npi', models.IntegerField()),
                ('specialty_description', models.CharField(max_length=100)),
                ('bene_count_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('bene_count_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('bene_count_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('bene_count_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('bene_count_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('bene_count_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_claim_count_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_claim_count_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_claim_count_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_claim_count_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_claim_count_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_claim_count_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_30_day_fill_count_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_30_day_fill_count_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_30_day_fill_count_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_30_day_fill_count_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_30_day_fill_count_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_30_day_fill_count_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_day_supply_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_day_supply_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_day_supply_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_day_supply_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_day_supply_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_day_supply_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_drug_cost_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_drug_cost_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_drug_cost_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_drug_cost_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_drug_cost_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('total_drug_cost_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Services_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Services_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Services_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Services_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Services_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Services_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Medicare_Beneficiaries_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Medicare_Beneficiaries_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Medicare_Beneficiaries_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Medicare_Beneficiaries_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Medicare_Beneficiaries_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Medicare_Beneficiaries_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Distinct_Medicare_Beneficiary_Per_Day_Services_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Submitted_Charge_Amount_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Submitted_Charge_Amount_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Submitted_Charge_Amount_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Submitted_Charge_Amount_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Submitted_Charge_Amount_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Submitted_Charge_Amount_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Medicare_Payment_Amount_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Medicare_Payment_Amount_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Medicare_Payment_Amount_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Medicare_Payment_Amount_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Medicare_Payment_Amount_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Medicare_Payment_Amount_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Suppliers_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Suppliers_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Suppliers_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Suppliers_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Suppliers_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Suppliers_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Beneficiaries_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Beneficiaries_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Beneficiaries_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Beneficiaries_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Beneficiaries_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Beneficiaries_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Claims_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Claims_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Claims_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Claims_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Claims_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Claims_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Services_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Services_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Services_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Services_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Services_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Number_of_Supplier_Services_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Submitted_Charge_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Submitted_Charge_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Submitted_Charge_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Submitted_Charge_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Submitted_Charge_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Submitted_Charge_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Medicare_Payment_Amount_mean', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Medicare_Payment_Amount_min', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Medicare_Payment_Amount_max', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Medicare_Payment_Amount_sum', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Medicare_Payment_Amount_median', models.DecimalField(decimal_places=10, max_digits=100)),
                ('Average_Supplier_Medicare_Payment_Amount_std', models.DecimalField(decimal_places=10, max_digits=100)),
                ('claimid', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(default='notsuspicious', max_length=50)),
                ('documentver', models.CharField(default='ND', max_length=10)),
            ],
        ),
    ]